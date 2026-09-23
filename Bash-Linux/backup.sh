#!/bin/bash

# Check if the correct number of arguments is provided
if [[ $# != 2 ]]
then
  echo "Usage: ./backup.sh <target_directory_name> <destination_directory_name>"
  exit 1
fi

# Validate directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Error: Invalid directory path provided."
  exit 1
fi

# Assign target and destination variables
targetDirectory=$1
destinationDirectory=$2

echo "Target Directory is $targetDirectory"
echo "Destination Directory is $destinationDirectory"

# Define backup filename with current timestamp
currentTS=$(date +%s)
backupFileName="backup-$currentTS.tar.gz"

# Save absolute paths for navigation
origAbsPath=$(pwd)
cd "$destinationDirectory"
destAbsPath=$(pwd)

# Navigate to target directory to find files to backup
cd "$origAbsPath"
cd "$targetDirectory"

# Calculate timestamp for 24 hours ago
yesterdayTS=$(date -d "yesterday" +%s)

declare -a toBackup

# Identify files modified within the last 24 hours
for file in * 
do
  if [[ `date -r $file +%s` -gt $yesterdayTS ]]
  then
    toBackup+=("$file")
  fi
done

# Compress selected files into a backup archive
tar -czvf $backupFileName${toBackup[@]}

# Move the completed backup to the destination directory
mv $backupFileName$destAbsPath

echo "Backup completed successfully."
