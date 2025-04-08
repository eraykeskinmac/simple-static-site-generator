#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the main script
python3 "$SCRIPT_DIR/src/main.py"

# Start a web server in the public directory
cd "$SCRIPT_DIR/public"
python3 -m http.server 8888