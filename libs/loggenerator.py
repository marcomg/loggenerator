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

def addTextInFrame(text):
    global log
    leng = len(text)
    log += "\n" + text + "\n" + '-' * leng + "\n"

def addCommand(command, h = True):
    if h:
        addTextInFrame('Command: ' + command)
    global log
    try:
        out = subprocess.check_output(command, shell=True, universal_newlines=True)
        log += str(out)
    except subprocess.CalledProcessError:
        pass

def addFile(fileP):
    addTextInFrame('File: ' + fileP)
    addCommand('cat ' + fileP, False)

def addDir(directory):
    addTextInFrame('Direcotry: ' + directory)
    files = _getRecoursiveFileList(directory)
    for myfile in files:
        addFile(myfile)

def addDirList(directory):
    addTextInFrame('Direcotry list: ' + directory)
    global log
    files = _getRecoursiveFileList(directory)
    for tfile in files:
        log += tfile + "\n"

def isPackageInstalled(package):
    addCommand('dpkg -l | grep -i "%s"' % (package))

def logWrite(f):
    global log
    f.write(log)