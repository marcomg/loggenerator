#!/usr/bin/python3
# Standard library
import sys
import os
import getpass
import time
import lzma

# Personal library
sys.path.append('libs')  # questa linea solo se non pacchettizato
import constants
import pastedebian
import simpleprompt
import loggenerator
import fileHandler
import problemType

# exit function
def programExit():
    if os.path.isfile(constants.fileLogName):
        print('Il file di log é: ' + constants.fileLogName)
    else:
        print('Nessun file di log creato')
        
    if os.path.isfile(constants.compFileLogName):
        print('Il file compresso é: ' + constants.compFileLogName)
    else:
        print('Nessun file compresso del log creato')
        
    exit()

# Clear screen
os.system('clear')

# Intro
print(constants.programIntroString)

# Chiedo conferma
print(constants.programAdviceStrings)
if not simpleprompt.boolQuestionY('Continuare?'):
    programExit()

# Controllo di essere root
if getpass.getuser() != 'root':
    print(constants.errorStringRoot)
    programExit()

# Seleziono il tipo di problema
problem = simpleprompt.multiChoose(constants.menuItemsStrings,
                                   constants.menuItemsQuestion)

# Genero i log
# 0 esci
if problem == 0:
    programExit()
    
myProblem = problemType.problem()

# 7 commons (da eseguire sempre tranne che allo 0) e altro tipo di problemi
if 1 <= problem <= len(constants.menuItemsStrings)-1:
    myProblem.commandsCommon()
    
# 1 problemi relativi alle connessioni di rete
if problem == 1:
    myProblem.commandsNetwork()
    
# 2 problemi video
elif problem == 2:
    myProblem.commandsVideo()
    
# 3 problemi audio
elif problem == 3:
    myProblem.commandsAudio()
        
# 4 problemi di gestione dei pacchetti (APT)
elif problem == 4:
    myProblem.commandsAPT()
    
# 5 problemi di mount/unmount
elif problem == 5:
    myProblem.commandsMount()
    
# 6 problemi di funzionamento del touchpad
elif problem == 6:
    myProblem.commandsTouchpad()


# myfile is an object of the class "fileOps" in fileHandler(.py) module
myfile = fileHandler.FileOps(constants.fileLogName)
myfile.go()

# Invio i logs a paste.debian.net
if simpleprompt.boolQuestion('Vuoi inviare i logs su paste.debian.net?'):
    print('Invio in corso, attendere...')
    links = []
    f = open(fileLogName, 'r')
    while True:
        tmp = f.readlines(100 * 1024)  # 100 KiB
        tmp = ''.join(tmp)
        if tmp == '':
            break
        else:
            links.append(pastedebian.addPaste(tmp, expire=60 * 60 * 24 * 30)['view_url'])  # i links scadono dopo un mese
    print('invio completato. I links sono:')
    for link in links:
        print(link)
        
        
# Log compression
if simpleprompt.boolQuestionY('Creare un file compresso del log?'):
    with open(constants.fileLogName, 'rb') as logfile:
        compressData = logfile.read()
        with lzma.open(constants.compFileLogName, 'w') as complogfile:
            complogfile.write(compressData)
            
            
programExit()            
    
    
    
    
    
    
    
    
    
       
