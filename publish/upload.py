import os

key_repo_user = "PYPI_REPO_USER"
key_repo_pass = "PYPI_REPO_PASS"


def load_credentials():
    if key_repo_user in os.environ and key_repo_pass in os.environ:
        repo_user = os.environ[key_repo_user]
        repo_pass = os.environ[key_repo_pass]
        return repo_user, repo_pass
    else:
        print(f"OS Environ: {os.environ}")
        raise Exception(
            f"Environment variables for uploading to PyPI not found: {key_repo_user} and {key_repo_pass}. "
            f"Please create an account at https://pypi.org",
        )


def upload_distribution():
    repo_user, repo_pass = load_credentials()
    command = f"pip install twine && twine upload -u {repo_user} -p {repo_pass} dist/*"
    os.system(command)


upload_distribution()
