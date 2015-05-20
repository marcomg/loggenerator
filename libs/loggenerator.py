import subprocess
import os
import os.path
import re
import shutil
import constants

class functions():
    log = ''
    
    def _getRecoursiveFileList(self, rootdir):
        fileList = []
        for root, subFolders, files in os.walk(rootdir):
            for f in files:
                fileList.append(os.path.join(root, f))
        return fileList;
    
    # Checks if a file exists
    # Returns 1 if a file exists, 0 otherwise
    def _ifFileExists(self, filename):
        if os.path.isfile(filename):
            return 1
        return 0
    
    # Checks if a directory exists
    # Returns 1 if a directory exists, 0 otherwise
    def _ifDirExists(self, dirname):
        if os.path.isdir(dirname):
            return 1
        return 0
    
    # Deletes options (if any) from a command
    # Returns only command 
    def stripOptions(self, string):
        command = re.search('(.*) *', string)
        return command.group(0)
    
    
    # Output message based on the second parameter
    def printOnScreen(self, string, type):
        if type == 'f':
            print('File: ' + string)
        elif type == 'd':
            print('Directory: ' + string)
        elif type == 'c':
            print('Comando: ' + string) 
    
    
    def addTextInFrame(self, text):
        leng = len(text)
        self.__class__.log += "\n" + text + "\n" + '-' * leng + "\n"
    
    def addCommand(self, command, h=True):
        self.printOnScreen(command, 'c')
        trash = open(os.devnull, 'w')  # file to put standard error
        if h:
            self.addTextInFrame('Command: ' + command)
        try:
            command1 = self.stripOptions(command)
            if shutil.which(command1) != 'None':
                if command == 'groups':
                    out = subprocess.check_output('su ' + constants.utente + ' -c ' + command, shell=True, universal_newlines=True, stderr=trash)
                    self.__class__.log += str(out)
                else:
                    out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)
                    self.__class__.log += str(out)
        except subprocess.CalledProcessError:
            pass
    
    def addFile(self, fileP):
        self.printOnScreen(fileP, 'f')
        self.addTextInFrame('File: ' + fileP)
        if self._ifFileExists(fileP):
            with open(fileP, 'r') as myfile:
                content = myfile.read()                                     # file content in a variable
            
                # syslog
                if fileP == '/var/log/syslog':
                    myre = re.compile('.*rsyslogd.*start')                  # regular expression (RE)
                    try:
                        header = myre.findall(content)[-1]                  # search the last occurence [-1] of previous RE
                        string1 = myre.split(content)[-1]                   # last block (from 'header' to the end of file)
                        string2=''                                          # syslog.1 not considered
                        
                    except IndexError:                                      # RE can't match anything    
                        with open('/var/log/syslog.1', 'r') as myfile2:     # open syslog.1 
                            content2 = myfile2.read()                       # syslog.1 content in a variable
                            header = myre.findall(content2)[-1]             
                            string2 = myre.split(content2)[-1]
                            string1 = content                               # string1 contains entire syslog 
    
                         
                    self.__class__.log = ''.join((self.__class__.log, header, string2, string1))          # join four strings
                
                # all other files   
                else:
                    self.__class__.log = ''.join((self.__class__.log, content))
        else:
            self.__class__.log = ''.join((self.__class__.log, 'File non trovato\n'))
    
    
    def addDir(self, directory):
        self.printOnScreen(directory, 'd')
        self.addTextInFrame('Directory: ' + directory)
        if self._ifDirExists(directory):
            files = self._getRecoursiveFileList(directory)
            for myfile in files:
                self.addFile(myfile)
    
    def addDirList(self, directory):
        self.printOnScreen(directory, 'd')
        self.addTextInFrame('Directory list: ' + directory)
        files = self._getRecoursiveFileList(directory)
        for tfile in files:
            self.__class__.log += tfile + "\n"
    
    def isPackageInstalled(self, package):
        self.addCommand('dpkg -l | grep -i "%s"' % (package))
    
    def isDeamonRunning(self, deamon):
        self.addTextInFrame('Deamon: ' + deamon)
        self.addCommand('invoke-rc.d "%s" status' % (deamon), False)
    
    def getLogFile(self):
        return self.__class__.log
