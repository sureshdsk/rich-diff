# -*- coding: utf-8 -*-
import os
from shutil import rmtree


def remove_artifacts(path):
    if os.path.exists(path):
        rmtree(path)
        print(f"Removed: {path}")


remove_artifacts("build")
remove_artifacts("dist")
remove_artifacts("src")

egg_paths = [x for x in os.listdir() if ".egg-info" in x]
for x in egg_paths:
    remove_artifacts(x)
