# Constant values
# Constant string are in programStrings.py

import os
import os.path
import time
import socket

# Constant strings

programIntroString = '''
*********************************************************************************
*  www.debianizzati.org                                                         *
*                                                                               *
*  Script che crea un log utile alla risoluzione dei problemi più comuni        *
*  Sotto licenza GPLv3                                                          *
*                                                                               *
*********************************************************************************'''


programAdviceStrings = '''
-- Lo script richiede i permessi di root per essere eseguito
-- per inviare il log su paste.debian.net è necessaria una connessione ad internet,
-- l'invio del log a paste.debian.net avverrà solo dopo esplicito consenso.
-- Verrà creato un file contenente l'output di questo script e
-- verrà creato un file in formato compresso da inviare al forum.
-- I seguenti file verranno creati nella stessa directory dove verrà eseguito lo script
-- se i file di log esistono verranno sovrascritti.'''


menuItemsStrings = ['Problemi relativi alle connessioni di rete',
    'Problemi video',
    'Problemi audio',
    'Problemi di gestione dei pacchetti (APT)',
    'Problemi di mount/unmount',
    'Problemi di funzionamento del touchpad',
    'Altro tipo di problema',
    'Esci']


menuItemsQuestion = 'Select a number: '


errorStringRoot = 'Errore: lo script deve essere lanciato da root.'

# suite/codename correspondence
stable = 'jessie'
testing = 'stretch'

# accepted releases during search of external packages
# read above for stable/testing value
releases = ['sid']
releases.append(stable)
releases.append(testing)

# Words in this list are not hidden if they represent the current username/hostname
passList = ['Debian', 'debian', 'deb']

# username (!= root)
utente = os.getlogin()

# hostname
nomehost = socket.gethostname()


# Log file name based on the current date
fileLogName = 'log-' + time.strftime("%d%m%Y-%H%M%S")


# Compressed file name (.xz)
compFileLogName = fileLogName + '.xz'

# Check whether systemd is running
if os.path.isdir('/run/systemd/system'):
    SYSTEMD = True
else:
    SYSTEMD = False


