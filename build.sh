#!/bin/bash

# Get the repository name from the git remote URL
REPO_NAME=$(basename -s .git `git config --get remote.origin.url`)

# Run the generator with the correct GitHub Pages URL
python3 src/main.py "https://eraykeskinmac.github.io/$REPO_NAME/" 