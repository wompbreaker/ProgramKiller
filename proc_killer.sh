#!/bin/bash

# Navigate to the directory of the script
cd "$(dirname "$0")"

# Run the Python script in the background
python3 monitor.py &

# Check the exit status of the command
if [ $? -ne 0 ]; then
    echo "An error occurred while running the script. Error code: $?"
else
    echo "Script is running in the background."
fi
