#!/bin/bash

# Get the repository name from the git remote URL
REPO_NAME=$(basename -s .git `git config --get remote.origin.url`)

# Run the generator with the correct basepath
python3 src/main.py "/$REPO_NAME/" 