# backup_files
Backing up Home folder using rsync


`secrets.zsh` example file
```zsh
#!/bin/zsh

# System Info, depends on the sysmte
export OS_NAME=$(lsb_release -si)
export OS_VERSION=$(lsb_release -sr)
export HOSTNAME=$(hostname)

# Directories
export dest_backupdir=user@ip:/path/to/destination/$HOSTNAME-$OS_NAME-$OS_VERSION
export source_backupdir=/home/user/

# Telegram Bot Info
export TELEGRAM_BOT_TOKEN="123456789:ADWDAWDADADWDADAWDADWD"
export CHAT_ID="123456789"
```
