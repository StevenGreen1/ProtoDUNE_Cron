#!/bin/bash

#Setup
source setup.sh

export DIRECTORY=$1
export CONCATENATED_FILE=$2
export TEST_BEAM_MODE=$3

echo $1
echo $2
echo $3
# Merge to single ROOT file
root -b -l > /dev/null << EOF
.L ${CRON_HOME}/MergeTrees.C
MergeTrees("Validation", "${DIRECTORY}/tmp_*.root", "${CONCATENATED_FILE}")
.q
EOF

cp ${CONCATENATED_FILE} ${DIRECTORY}

# Process
root -b -l << EOF
.L ${CRON_HOME}/LArReco/validation/Validation.C+
.L ${CRON_HOME}/Process.C
Process("${DIRECTORY}", "${CONCATENATED_FILE}", "${TEST_BEAM_MODE}")
.q
EOF

rm ${CONCATENATED_FILE}
rm ${DIRECTORY}/tmp*.root;
