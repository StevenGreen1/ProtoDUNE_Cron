#!/usr/bin/python
import os
import re
import random
import dircache
import sys
import datetime
import subprocess

#==================

def generate(parameters):
    jobList = ''
    for eventSelection in parameters:
        eventType = eventSelection['EventType']
        eventsPerFile = eventSelection['EventsPerFile']
        detectorModel = eventSelection['DetectorModel']
        sample = eventSelection['Sample']
        larsoftVersion = eventSelection['LArSoftVersion']
        spaceChargeOn = eventSelection['SpaceChargeEffect']
        pandoraSetttingsFiles = eventSelection['PandoraSettingsFiles']
        cwd = eventSelection['cwd']
        settingsLocation = eventSelection['SettingsLocation']
        outputPath = eventSelection['OutputPath']
        maxEventsToProcess = eventSelection['MaxEventsToProcess']
        now = eventSelection['Now']

        for momenta in eventSelection['Momentum']:
            spaceChargeString = ''
            if spaceChargeOn:
                spaceChargeString = 'SpaceChargeEffectOn'
            else:
                spaceChargeString = 'SpaceChargeEffectOff'

            pndrPath = '/r05/dune/protoDUNE/' + sample + '_Pndr/' + detectorModel + '/LArSoft_Version_' + larsoftVersion + '/' + eventType + '/' + str(momenta) + 'GeV/' + spaceChargeString + '/'
            pndrFormat = sample + '_Pndr_' + detectorModel + '_LArSoft_Version_' + larsoftVersion + '_Beam_Cosmics_Momentum_' + str(momenta) + 'GeV_(.*?).pndr'

            settingsPath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/PandoraSettings')
            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/RootFiles')

            if not os.path.exists(settingsPath):
                os.makedirs(settingsPath)

            if not os.path.exists(rootFilePath):
                os.makedirs(rootFilePath)

            baseContent = {}

            for settingsName, settingsFile in pandoraSetttingsFiles.items():
                baseFile = os.path.join(settingsLocation, settingsFile)
                base = open(baseFile,'r')
                baseContent[settingsName] = base.read()
                base.close()

            fileDirectory = pndrPath
            allFilesInDirectory = dircache.listdir(fileDirectory)
            inputFileExt = 'pndr'

            allFiles = []
            allFiles.extend(allFilesInDirectory)
            allFiles[:] = [ item for item in allFiles if re.match('.*\.' + inputFileExt + '$',item.lower()) ]
            allFiles.sort()

            nFiles = 0
            eventCounter = 0
            if allFiles:
                nFiles = len(allFiles)

            for idx in range (nFiles):
                if eventCounter > maxEventsToProcess:
                    continue

                nextFile = allFiles.pop(0)
                matchObj = re.match(pndrFormat, nextFile, re.M|re.I)

                if matchObj:
                    identifier = matchObj.group(1)
                    eventCounter += eventsPerFile

                    newSettingsName = {}
                    for settingsName in pandoraSetttingsFiles:
                        newSettingsName[settingsName] = os.path.splitext(pandoraSetttingsFiles[settingsName])[0] + '_' + str(identifier) + '.xml'

                    for settingsName, settingsFileContent in baseContent.items():
                        newContent = settingsFileContent
                        settingsFullPath = os.path.join(settingsPath, newSettingsName[settingsName])

                        #==========
                        # This is where to modify the files
                        #==========
                        if settingsName == 'Master':
                            rootFileFullPath = os.path.join(rootFilePath, 'tmp_EventValidation_Job_Number_' + str(identifier) + '.root')
                            newContent = re.sub('Validation.root', rootFileFullPath, newContent)
                            newContent = re.sub('<algorithm type = "LArVisualMonitoring">((.|\n)*?)</algorithm>', '', newContent)
                            newContent = re.sub('<WriteToTree>(.*?)</WriteToTree>', '<WriteToTree>true</WriteToTree>', newContent)

                            jobList += settingsFullPath + ' ' + os.path.join(pndrPath,nextFile)
                            jobList += '\n'
                        #==========

                        file = open(settingsFullPath,'w')
                        file.write(newContent)
                        file.close()
                        del newContent

    runFile = open(os.path.join(cwd, 'RunFile.txt') ,'w')
    runFile.write(jobList)
    runFile.close()

#==================

def run():
    with open('RunFile.txt') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for args in content:
        args = args.split()
        args.insert(0, os.path.join(os.getcwd(), 'LArReco.sh'))
        process = subprocess.Popen(args)
        process.wait()

#==================

def update():
    process = subprocess.Popen([os.path.join(os.getcwd(), 'update.sh')])
    process.wait()

#==================

def build():
    process = subprocess.Popen([os.path.join(os.getcwd(), 'build.sh')])
    process.wait()

#==================

def results(parameters):
    for eventSelection in parameters:
        eventType = eventSelection['EventType']
        spaceChargeOn = eventSelection['SpaceChargeEffect']
        outputPath = eventSelection['OutputPath']
        now = eventSelection['Now']
        cwd = eventSelection['cwd']

        for momenta in eventSelection['Momentum']:
            spaceChargeString = ''
            if spaceChargeOn:
                spaceChargeString = 'SpaceChargeEffectOn'
            else:
                spaceChargeString = 'SpaceChargeEffectOff'

            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/RootFiles')
            concatenatedFile = "EventValidation_" + str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '_' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '_Concatenated.root'

            process = subprocess.Popen([os.path.join(os.getcwd(), 'results.sh'), rootFilePath, concatenatedFile])
            process.wait()
