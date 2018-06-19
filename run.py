#!/usr/bin/python
from cron import *

#===========================
# Input Variables
#===========================

parameters = [
                { 'PandoraSettingsFiles': {'Master' : 'PandoraSettings_Master_ProtoDUNE.xml'},
                  'EventType': "Beam_Cosmics",
                  'EventsPerFile' : 10,
                  'Momentum':  [5],
                  'DetectorModel': 'ProtoDUNE-SP',
                  'Sample': 'mcc10',
                  'LArSoftVersion': 'larsoft_v06_63_00_triggered_mc_info',
                  'SpaceChargeEffect': False,
                  'cwd' : os.getcwd(),
                  'SettingsLocation' : os.path.join(os.getcwd(), 'LArReco/settings'),
                  'OutputPath' : '/r05/dune/sg568/LAr/Cron',
                  'MaxFilesToProcess' : 10,
                  'Now' : datetime.datetime.now()
                }
             ]

#update()
#build()
#generate(parameters)
#run()
results(parameters)

