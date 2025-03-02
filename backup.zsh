#!/bin/zsh

source ./secrets.zsh

echo 
echo "=======================backup $(date)======================="
echo 
echo "destination: $dest_backupdir"
echo "source: $source_backupdir"
echo


rsync -rltvz --exclude-from=exclude-list.txt -e "sudo -u $user_impersonate ssh" $source_backupdir $dest_backupdir --delete

EXIT_CODE=$?


MESSAGE="Backup from $HOSTNAME ($OS_NAME $OS_VERSION) completed.\nRsync Exit Code: $EXIT_CODE"
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
     -H "Content-Type: application/json" \
     -d "{\"chat_id\": \"$CHAT_ID\", \"text\": \"$MESSAGE\"}"


echo 
echo "=======================end of backup======================="
exit $EXIT_CODE
