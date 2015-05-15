import subprocess
import os
import os.path
import re
import shutil
import constants

def _getRecoursiveFileList(rootdir):
    fileList = []
    for root, subFolders, files in os.walk(rootdir):
        for f in files:
            fileList.append(os.path.join(root, f))
    return fileList;

# Checks if a file exists
# Returns 1 if a file exists, 0 otherwise
def _ifFileExists(filename):
    if os.path.isfile(filename):
        return 1
    return 0

# Checks if a directory exists
# Returns 1 if a directory exists, 0 otherwise
def _ifDirExists(dirname):
    if os.path.isdir(dirname):
        return 1
    return 0

# Deletes options (if any) from a command
# Returns only command 
def stripOptions(string):
    command = re.search('(.*) *', string)
    return command.group(0)


# Output message based on the second parameter
def printOnScreen(string, type):
    if type == 'f':
        print('File: ' + string)
    elif type == 'd':
        print('Directory: ' + string)
    elif type == 'c':
        print('Comando: ' + string) 

log = ''

def addTextInFrame(text):
    global log
    leng = len(text)
    log += "\n" + text + "\n" + '-' * leng + "\n"

def addCommand(command, h=True):
    printOnScreen(command, 'c')
    trash = open(os.devnull, 'w')  # file to put standard error
    if h:
        addTextInFrame('Command: ' + command)
    global log
    try:
        command1 = stripOptions(command)
        if shutil.which(command1) != 'None':
            if command == 'groups':
                out = subprocess.check_output('su ' + constants.utente + ' -c ' + command, shell=True, universal_newlines=True, stderr=trash)
                log += str(out)
            else:
                out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)
                log += str(out)
    except subprocess.CalledProcessError:
        pass

def addFile(fileP):
    printOnScreen(fileP, 'f')
    addTextInFrame('File: ' + fileP)
    if _ifFileExists(fileP):
        global log
        with open(fileP, 'r') as myfile:
            log += myfile.read()


def addDir(directory):
    printOnScreen(directory, 'd')
    addTextInFrame('Directory: ' + directory)
    if _ifDirExists(directory):
        files = _getRecoursiveFileList(directory)
        for myfile in files:
            addFile(myfile)

def addDirList(directory):
    printOnScreen(directory, 'd')
    addTextInFrame('Directory list: ' + directory)
    global log
    files = _getRecoursiveFileList(directory)
    for tfile in files:
        log += tfile + "\n"

def isPackageInstalled(package):
    addCommand('dpkg -l | grep -i "%s"' % (package))

def isDeamonRunning(deamon):
    addTextInFrame('Deamon: ' + deamon)
    addCommand('invoke-rc.d "%s" status' % (deamon), False)

def getLogFile():
    return log
