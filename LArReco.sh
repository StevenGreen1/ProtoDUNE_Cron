#!/bin/bash

# Setup
source setup.sh

export FW_SEARCH_PATH=${FW_SEARCH_PATH}:"$CRON_HOME/LArReco/settings":"$CRON_HOME/LArMachineLearningData"
export PD_GEOEMTRY="$CRON_HOME/LArReco/geometry/PandoraGeometry_ProtoDUNE.xml"

$CRON_HOME/LArReco/bin/PandoraInterface -r Full -i $1 -e $2 -g ${PD_GEOEMTRY}

