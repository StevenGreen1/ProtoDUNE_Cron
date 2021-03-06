#!/usr/bin/python
from cron import *

#===========================
# Input Variables
#===========================

path = '/usera/sg568/LAr/Cron'
os.chdir(path)

parameters = [
                { 'JobName' : "ProtoDUNE",
                  'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_ProtoDUNE.xml'},
                  'EventType': "Beam_Cosmics",
                  'EventsPerFile' : 40,
                  'Momentum':  [5],
                  'DetectorModel': 'ProtoDUNE-SP',
                  'Sample': 'mcc10',
                  'LArSoftVersion': 'larsoft_v06_81_00',
                  'SpaceChargeEffect': True,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron',
                  'MaxEventsToProcess' : 600,
                  'Now' : datetime.datetime.now()
                }
             ]

update()
build()
generate(parameters)
run(parameters)
results(parameters)

