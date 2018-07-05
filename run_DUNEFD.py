#!/usr/bin/python
from cron import *

#===========================
# Input Variables
#===========================

#path = '/usera/sg568/LAr/Cron_DUNEFD'
#os.chdir(path)

#======================================================
# Electron Neutrinos, Muon Neutrinos and Anti-Neutrinos
#======================================================

parameters = [
                { 'JobName' : "DUNEFD",
                  'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_DUNEFD.xml'},
                  'EventType': "nue",
                  'EventsPerFile' : 200,
                  'DetectorModel': 'DUNEFD_dune10kt_1x2x6',
                  'Sample': 'mcc10',
                  'LArSoftVersion': 'larsoft_v06_60_00',
                  'SpaceChargeEffect': False,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron_DUNEFD',
                  'MaxEventsToProcess' : 20000,
                  'Now' : datetime.datetime.now()
                },
                { 'JobName' : "DUNEFD",
                  'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_DUNEFD.xml'},
                  'EventType': "numu",
                  'EventsPerFile' : 200,
                  'DetectorModel': 'DUNEFD_dune10kt_1x2x6',
                  'Sample': 'mcc10',
                  'LArSoftVersion': 'larsoft_v06_60_00',
                  'SpaceChargeEffect': False,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron_DUNEFD',
                  'MaxEventsToProcess' : 20000,
                  'Now' : datetime.datetime.now()
                },
                { 'JobName' : "DUNEFD",
                  'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_DUNEFD.xml'},
                  'EventType': "anu",
                  'EventsPerFile' : 200,
                  'DetectorModel': 'DUNEFD_dune10kt_1x2x6',
                  'Sample': 'mcc10',
                  'LArSoftVersion': 'larsoft_v06_60_00',
                  'SpaceChargeEffect': False,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron_DUNEFD',
                  'MaxEventsToProcess' : 20000,
                  'Now' : datetime.datetime.now()
                }
             ]

update()
build()
generate(parameters)
run(parameters)
results(parameters)

