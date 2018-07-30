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
        detectorModel = eventSelection['DetectorModel']
        sample = eventSelection['Sample']
        larsoftVersion = eventSelection['LArSoftVersion']
        spaceChargeOn = eventSelection['SpaceChargeEffect']
        cwd = eventSelection['cwd']
        outputPath = eventSelection['OutputPath']
        now = eventSelection['Now']

        spaceChargeString = ''
        if spaceChargeOn:
            spaceChargeString = 'SpaceChargeEffectOn'
        else:
            spaceChargeString = 'SpaceChargeEffectOff'

        if "ProtoDUNE" in eventSelection['JobName']:
            for momenta in eventSelection['Momentum']:
                pndrPath = '/r05/dune/protoDUNE/' + sample + '_Pndr/' + detectorModel + '/LArSoft_Version_' + larsoftVersion + '/' + eventType + '/' + str(momenta) + 'GeV/' + spaceChargeString + '/'
                pndrFormat = sample + '_Pndr_' + detectorModel + '_LArSoft_Version_' + larsoftVersion + '_Beam_Cosmics_Momentum_' + str(momenta) + 'GeV_(.*?).pndr'
                settingsPath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/PandoraSettings')
                rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/RootFiles')

                jobParameters = {}
                jobParameters['PndrPath'] = pndrPath
                jobParameters['PndrFormat'] = pndrFormat
                jobParameters['SettingsPath'] = settingsPath
                jobParameters['RootFilePath'] = rootFilePath

                jobListString = generateJobFiles(eventSelection, jobParameters)
                jobList += jobListString

        elif "DUNEFD" in eventSelection['JobName']:
            pndrPath = '/r05/dune/DUNEFD/' + sample + '_Pndr/' + detectorModel + '/LArSoft_Version_' + larsoftVersion + '/' + eventType + '/' + spaceChargeString + '/'
            pndrFormat = 'Pandora_Events_(.*?).pndr'
            settingsPath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/PandoraSettings')
            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/RootFiles')

            jobParameters = {}
            jobParameters['PndrPath'] = pndrPath
            jobParameters['PndrFormat'] = pndrFormat
            jobParameters['SettingsPath'] = settingsPath
            jobParameters['RootFilePath'] = rootFilePath

            jobListString = generateJobFiles(eventSelection, jobParameters)
            jobList += jobListString

        elif "MicroBooNE" in eventSelection['JobName']:
            pndrPath = '/r05/dune/MicroBooNE/' + sample + '_Pndr/' + detectorModel + '/LArSoft_Version_' + larsoftVersion + '/' + eventType + '/' + spaceChargeString + '/'
            pndrFormat = 'Pandora_Events_(.*?).pndr'
            settingsPath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/PandoraSettings')
            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/RootFiles')

            jobParameters = {}
            jobParameters['PndrPath'] = pndrPath
            jobParameters['PndrFormat'] = pndrFormat
            jobParameters['SettingsPath'] = settingsPath
            jobParameters['RootFilePath'] = rootFilePath

            jobListString = generateJobFiles(eventSelection, jobParameters)
            jobList += jobListString

    runFile = open(os.path.join(cwd, 'RunFile.txt') ,'w')
    runFile.write(jobList)
    runFile.close()

#==================

def generateJobFiles(eventSelection, jobParameters):
    pandoraSetttingsFiles = eventSelection['PandoraSettingsFiles']
    maxEventsToProcess = eventSelection['MaxEventsToProcess']
    eventsPerFile = eventSelection['EventsPerFile']
    settingsLocation = eventSelection['SettingsLocation']

    pndrPath = jobParameters['PndrPath']
    pndrFormat = jobParameters['PndrFormat']
    settingsPath = jobParameters['SettingsPath']
    rootFilePath = jobParameters['RootFilePath']

    if not os.path.exists(settingsPath):
        os.makedirs(settingsPath)

    if not os.path.exists(rootFilePath):
        os.makedirs(rootFilePath)

    jobList = ''

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
                    newContent = re.sub('<IsMonitoringEnabled>(.*?)</IsMonitoringEnabled>', '<IsMonitoringEnabled>true</IsMonitoringEnabled>', newContent)
                    newContent = re.sub('<algorithm type = "LArVisualMonitoring">((.|\n)*?)</algorithm>', '', newContent)
                    newContent = re.sub('<WriteToTree>(.*?)</WriteToTree>', '<WriteToTree>true</WriteToTree>', newContent)
                    newContent = re.sub('<PrintAllToScreen>(.*?)</PrintAllToScreen>', '<PrintAllToScreen>false</PrintAllToScreen>', newContent)
                    newContent = re.sub('<PrintMatchingToScreen>(.*?)</PrintMatchingToScreen>', '<PrintMatchingToScreen>false</PrintMatchingToScreen>', newContent)

                    jobList += settingsFullPath + ' ' + os.path.join(pndrPath,nextFile)
                    jobList += '\n'
                #==========

                file = open(settingsFullPath,'w')
                file.write(newContent)
                file.close()
                del newContent

    return jobList

#==================

def run(parameters):
    commandString = ''
    geometryFile = ''

    isProtoDUNE = False
    isDUNEFD = False
    isMicroBooNE = False

    for eventSelection in parameters:
        if "ProtoDUNE" in eventSelection['JobName']:
            commandString = 'full'
            geometryFile = 'LArReco/geometry/PandoraGeometry_ProtoDUNE.xml'
            isProtoDUNE = True

        elif "DUNEFD" in eventSelection['JobName']:
            commandString = 'allhitsnu'
            geometryFile = 'LArReco/geometry/PandoraGeometry_DUNEFD_1x2x6.xml'
            isDUNEFD = True

        elif "MicroBooNE" in eventSelection['JobName']:
            commandString = 'allhitsnu' # No cosmics in paper sample
            geometryFile = 'LArReco/geometry/PandoraGeometry_MicroBooNE_MCC7Gaps.xml' # Valid for paper samples
            isMicroBooNE = True

    if [isProtoDUNE, isDUNEFD, isMicroBooNE].count(True) != 1:
        print("Attempting to run cron job for either no detector or multiple detectors")
        sys.exit()

    with open('RunFile.txt') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    for args in content:
        args = args.split()
        args.insert(0, os.path.join(os.getcwd(), 'LArReco.sh'))
        args.append(commandString)
        args.append(geometryFile)
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
        sample = eventSelection['Sample']
        larsoftVersion = eventSelection['LArSoftVersion']
        eventType = eventSelection['EventType']
        spaceChargeOn = eventSelection['SpaceChargeEffect']
        outputPath = eventSelection['OutputPath']
        now = eventSelection['Now']
        cwd = eventSelection['cwd']

        spaceChargeString = ''
        if spaceChargeOn:
            spaceChargeString = 'SpaceChargeEffectOn'
        else:
            spaceChargeString = 'SpaceChargeEffectOff'

        # ATTN: The thrid and fourth arguments of results.sh are isTestBeamMode and applyUbooneFiducialCuts
        if "ProtoDUNE" in eventSelection['JobName']:
            # ProtoDUNE Events
            for momenta in eventSelection['Momentum']:
                rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '/RootFiles')
                concatenatedFile = "EventValidation_" + str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '_' + sample + '_' + larsoftVersion + '_' + eventType + '_' + str(momenta) + 'GeV_' + spaceChargeString + '_Concatenated.root'
                process = subprocess.Popen([os.path.join(os.getcwd(), 'results.sh'), rootFilePath, concatenatedFile, 'true', 'false'])
                process.wait()

        elif "DUNEFD" in eventSelection['JobName']:
            # DUNEFD Events
            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/RootFiles')
            concatenatedFile = "EventValidation_" + str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '_' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '_Concatenated.root'
            process = subprocess.Popen([os.path.join(os.getcwd(), 'results.sh'), rootFilePath, concatenatedFile, 'false', 'false'])
            process.wait()

        elif "MicroBooNE" in eventSelection['JobName']:
            # MicroBooNE Events
            rootFilePath = os.path.join(outputPath, str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '/' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '/RootFiles')
            concatenatedFile = "EventValidation_" + str(now.strftime("%Y")) + '_' + now.strftime("%m") + '_' + now.strftime("%d") + '_' + sample + '_' + larsoftVersion + '_' + eventType + '_' + spaceChargeString + '_Concatenated.root'
            process = subprocess.Popen([os.path.join(os.getcwd(), 'results.sh'), rootFilePath, concatenatedFile, 'false', 'true'])
            process.wait()
