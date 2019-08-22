#!/bin/bash
source ./venv/bin/activate
gcloud iam service-accounts list --project  chariots-dbig  --format="value(reinaldomaslim)"
gcloud app deploy --quiet --project chariots-dbig