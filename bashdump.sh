DATE=$(date +%m-%d-%y\|%H:%M:%S)
DATABASE="nelsondb_test"
mysqldump $DATABASE  > /Users/sSDSD/bin/$DATABASE-BACKUP-[$DATE].sql
