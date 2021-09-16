import json
import os

# Bump the version.


def bump_version(config_file: str) -> str:

    # Open the file and read the version.
    with open(config_file, "r") as f:
        config_object = json.load(f)
        current_version = config_object["version"]
        versions = current_version.split(".")
        versions[-1] = str(int(versions[-1]) + 1)
        new_version = ".".join(versions)

    # Write the file back.
    with open(config_file, "w") as f:
        config_object["version"] = new_version
        json.dump(config_object, f, indent=2)

    # Return new version.
    print("Bumping Version Number: {} -> {}".format(current_version, new_version))
    return new_version


# Copy the version to the __init__.py file.
def copy_version_to_package(path: str, v: str):
    """Copy the single source of truth version number into the package as well."""

    # Copy __version__ to all root-level files in path.
    copy_files = ["__version__.py"]

    for file_name in copy_files:
        target_file = os.path.join(path, file_name)
        with open(target_file, "r") as original_file:
            lines = original_file.readlines()

        with open(target_file, "w") as new_file:
            for line in lines:
                if "__version__" not in line:
                    new_file.write(line)
                else:
                    new_file.write('__version__ = "{}"\n'.format(v))
