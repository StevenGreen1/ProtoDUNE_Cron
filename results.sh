#!/bin/bash

#Setup
source setup.sh

export DIRECTORY=$1
export CONCATENATED_FILE=$2

# Merge to single ROOT file
root -b -l > /dev/null << EOF
.L ${CRON_HOME}/MergeTrees.C
MergeTrees("Validation", "${DIRECTORY}/tmp_*.root", "${CONCATENATED_FILE}")
.q
EOF
rm ${DIRECTORY}/tmp*.root;

# Process
root -b -l << EOF
.L ${CRON_HOME}/LArReco/validation/Validation.C+
.L ${CRON_HOME}/Process.C
Process("${DIRECTORY}", "${CONCATENATED_FILE}")
.q
EOF

