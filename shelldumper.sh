#!/usr/bin/env bash

export PATH=$PATH:/usr/local/mysql/bin
DATE=$(date +%m-%d-%y\|%H:%M:%S)
DATABASE="nelsondb_test"

mysqldump $DATABASE  > /Users/sSDSD/bin/$DATABASE-[$DATE].sql
