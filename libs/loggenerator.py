import subprocess
import os
import os.path

def _getRecoursiveFileList(rootdir):
    fileList = []
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            fileList.append(os.path.join(root,file))
    return fileList;

log = ''

# Checks if a file exists
# Returns 1 if a file exists, 0 otherwise
def ifFileExists(filename):
    if os.path.isfile(filename):
        return 1
    return 0

# Checks if a directory exists
# Returns 1 if a directory exists, 0 otherwise
def ifDirExists(dirname):
    if os.path.isdir(dirname):
        return 1
    return 0

def addTextInFrame(text):
    global log
    leng = len(text)
    log += "\n" + text + "\n" + '-' * leng + "\n"

def addCommand(command, h = True):
    trash = open(os.devnull, 'w') # file to put standard error
    if h:
        addTextInFrame('Command: ' + command)
    global log
    try:
        out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)
        log += str(out)
    except subprocess.CalledProcessError:
        pass

def addFile(fileP):
    addTextInFrame('File: ' + fileP)
    if ifFileExists(fileP):
        addCommand('cat ' + fileP, False)

def addDir(directory):
    addTextInFrame('Directory: ' + directory)
    if ifDirExists(directory):
        files = _getRecoursiveFileList(directory)
        for myfile in files:
            addFile(myfile)

def addDirList(directory):
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