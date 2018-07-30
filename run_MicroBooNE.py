#!/usr/bin/python
from cron import *

#===========================
# Input Variables
#===========================

path = '/usera/sg568/LAr/Cron_MicroBooNE'
os.chdir(path)

#======================================================
# Electron Neutrinos, Muon Neutrinos and Anti-Neutrinos
#======================================================

parameters = [
                { 'JobName' : "MicroBooNE",
                  'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_MicroBooNE.xml'},
                  'EventType': "nu",
                  'EventsPerFile' : 1, # Find out
                  'DetectorModel': 'MicroBooNE',
                  'Sample': 'PandoraPaper',
                  'LArSoftVersion': 'larsoft_X', # Detailed in the paper
                  'SpaceChargeEffect': False,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron_MicroBooNE',
                  'MaxEventsToProcess' : 2,
                  'Now' : datetime.datetime.now()
                }
             ]

update()
build()
generate(parameters)
run(parameters)
results(parameters)

