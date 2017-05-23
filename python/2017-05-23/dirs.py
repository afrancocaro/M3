# !/usr/bin/python
# coding: utf-8

# Imports
import os

# Variables necessàries per al loop
pathToExplore = '/home/users/inf/hism1/ism46422801/workspace/git/M3/Imatges de la wiki'

# Loop per recórrer el directori
for path, dirs, files in os.walk(pathToExplore):

    print path
    print dirs
    print files
