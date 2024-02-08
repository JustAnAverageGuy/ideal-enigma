#!/bin/bash

set -xe
# Define the directory to monitor
directory_to_monitor="/home/aks/codin/cp/practice/jan_30/.qt/"

# Start monitoring the directory for file creation and deletion events
inotifywait -m -e create -e delete "$directory_to_monitor" | while read -r directory event filename; do
    if [[ "$event" == "CREATE" ]]; then
        echo "File created: $filename"
    elif [[ "$event" == "DELETE" ]]; then
        echo "File deleted: $filename"
        # Here you can choose to move the file to a different location
        # before it gets deleted. For example:
        mv "$directory$filename" "/home/aks/codin/cp/practice/jan_30/$filename"
    fi
done

