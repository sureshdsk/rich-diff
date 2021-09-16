# -*- coding: utf-8 -*-
import json
import os

import setuptools
from version_utils import bump_version
from version_utils import copy_version_to_package

# ======================================================================================================================
# Fill in this information for each package.
# ======================================================================================================================

CONFIG_FILE = "config.json"

# Load Config.
with open(CONFIG_FILE, "r") as config_file:
    config = json.load(config_file)

AUTHOR = config["author"]
EMAIL = config["email"]
DESCRIPTION = config["description"]
REPO = config["url"]
SCRIPTS = config["scripts"]
PYTHON_VERSION = config["python_version"]
PACKAGE_SRC = "../src"
PACKAGE_NAME_OVERRIDE = (
    None
    if "package_name_override" not in config or config["package_name_override"] is None
    else config["package_name_override"]
)

# ======================================================================================================================
# Discover the core package.
# ======================================================================================================================

# Work out the sources package.
src_paths = os.listdir(PACKAGE_SRC)
src_to_remove = [
    "__pycache__",
    "__init__.py",
    ".pytest_cache",
]

# Make sure we don't include this by accident.
for src_element in src_to_remove:
    if src_element in src_paths:
        src_paths.remove(src_element)

if len(src_paths) != 1:
    raise Exception(
        f"Failed to build: Source directory '{PACKAGE_SRC}' must contain exactly one Python package. "
        f"Instead, it contains {len(src_paths)}: {src_paths}",
    )

PACKAGE_NAME = src_paths[0]
PACKAGE_PATH = os.path.join(PACKAGE_SRC, PACKAGE_NAME)
print(f"Package Name Discovered: {PACKAGE_NAME}")
if PACKAGE_NAME_OVERRIDE is None:
    PACKAGE_NAME_OVERRIDE = PACKAGE_NAME


# ======================================================================================================================
# Automatic Package Setup Script.
# ======================================================================================================================

# Bump and copy the version.
version = bump_version(CONFIG_FILE)
copy_version_to_package(PACKAGE_PATH, version)

# Copy the README into the long description.
with open("../README.md", "r") as f:
    long_description = f.read()

packages = setuptools.find_packages(PACKAGE_SRC)
print(f"Packages Discovered: {packages}")

REQUIREMENTS_FILE = "../requirements.txt"
if os.path.exists(REQUIREMENTS_FILE):
    with open(REQUIREMENTS_FILE, "r") as f:
        requirement_packages = [line.strip("\n") for line in f.readlines()]
    print(f"Requirements: {requirement_packages}")
else:
    print(f"Requirements file not found at {REQUIREMENTS_FILE}")
    requirement_packages = []

setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    name=PACKAGE_NAME_OVERRIDE,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version,
    url=REPO,
    packages=packages,
    package_dir={PACKAGE_NAME: PACKAGE_PATH},
    install_requires=requirement_packages,
    classifiers=[f"Programming Language :: Python :: {PYTHON_VERSION}"],
    entry_points={"console_scripts": SCRIPTS},
)
