#!/bin/bash
 
SOURCE_DIR="/c/Users/307435/Documents/data"   
BACKUP_DIR="/c/Users/307435/Documents/backups"  
LOGFILE="$BACKUP_DIR/backup.log"
RETENTION_DAYS=7
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/backup_$DATE.tar.gz"
mkdir -p "$BACKUP_DIR"
if tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" . ; then
    echo "$DATE - SUCCESS: Backup created -> $BACKUP_FILE" | tee -a "$LOGFILE"
else
    echo "$DATE - ERROR: Backup failed!" | tee -a "$LOGFILE"
    exit 1
fi
find "$BACKUP_DIR" -maxdepth 1 -name "backup_*.tar.gz" -type f -mtime +$RETENTION_DAYS -exec rm -f {} \;
echo "$DATE - INFO: Old backups older than $RETENTION_DAYS days deleted." | tee -a "$LOGFILE"
