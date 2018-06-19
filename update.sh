#!/bin/bash

#Setup
source setup.sh

# Update
for i in PandoraSDK PandoraMonitoring LArContent LArReco LArMachineLearningData
do
    export DIRECTORY=$CRON_HOME/$i
    if [ -d "$DIRECTORY" ];
    then
        cd $CRON_HOME/$i
        git pull origin master
        cd $CRON_HOME
    else
        git clone https://github.com/PandoraPFA/${i}.git
    fi
done

cd $CRON_HOME
mkdir -p lib

