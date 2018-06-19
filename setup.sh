#!/bin/bash

# Setup
export CRON_HOME=`pwd`
source /cvmfs/uboone.opensciencegrid.org/products/setup_uboone.sh

setup gcc v4_9_3
setup git v2_4_6
setup eigen v3_3_3
setup root v6_06_08 -q e10:nu:prof

export LD_LIBRARY_PATH=${CRON_HOME}/lib/:$LD_LIBRARY_PATH
export PATH=${CRON_HOME}/LArReco/bin/:$PATH

