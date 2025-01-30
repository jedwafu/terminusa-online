#!/bin/bash

TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_DIR="/var/backups/terminusa"
DB_NAME="terminusa"

mkdir -p $BACKUP_DIR
pg_dump -U terminusa_admin -h localhost $DB_NAME | gzip > $BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql.gz

# Keep last 7 backups
ls -t $BACKUP_DIR/*.sql.gz | tail -n +8 | xargs rm -f