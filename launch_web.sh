#!/bin/bash
source ./venv/bin/activate

export GOOGLE_APPLICATION_CREDENTIALS=/home/rm/Downloads/chariots-dbig-b958016e566f.json
export CLOUD_SQL_CONNECTION_NAME='chariots-dbig:asia-southeast1:chariots-dbig-db'
export DB_USER='root'
export DB_PASS='aloha'
export DB_NAME='chariots'

gcloud app deploy --quiet --project chariots-dbig 
