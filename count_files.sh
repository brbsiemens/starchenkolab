#!/bin/bash

# Set the directory path
directory_path="/etc"

# Use find to count regular files (excluding directories and links)
file_count=$(find "$directory_path" -type f ! -type d ! -type l | wc -l)

# Print the result
echo "Number of regular files in $directory_path: $file_count"
