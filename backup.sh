#!/bin/bash
# directories to exclude
declare -a arr=(".local/lib/*"
		"Downloads/*")

dest_backupdir=/media/samsung/backup_pluton
source_backupdir=/home/matt/

echo
echo "destination:$dest_backupdir"
echo "source:$source_backupdir"
echo

for i in "${arr[@]}"
do
   excluded_dirs="$excluded_dirs --exclude=$i"
done

echo "excluding this directories:"
echo $excluded_dirs

rsync -ra $excluded_dirs $source_backupdir $dest_backupdir
