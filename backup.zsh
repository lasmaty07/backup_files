#!/bin/zsh

source ./secrets.sh

echo
echo "destination: $dest_backupdir"
echo "source: $source_backupdir"
echo

# Run rsync
rsync -rltvz --exclude-from=exclude-list.txt -e "ssh -i \"/home/matt/.ssh/id_ed25519\"" $source_backupdir $dest_backupdir --delete

EXIT_CODE=$?

# Send exit status to Telegram
MESSAGE="Backup from $HOSTNAME ($OS_NAME $OS_VERSION) completed.\nRsync Exit Code: $EXIT_CODE"
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
     -H "Content-Type: application/json" \
     -d "{\"chat_id\": \"$CHAT_ID\", \"text\": \"$MESSAGE\"}"

# Exit with rsync exit code
exit $EXIT_CODE
