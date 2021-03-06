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
        command = string.split()[0]
        return command
    
    
    # Output message based on the second parameter
    # f->file, d->directory, c->command. s->generic string
    def printOnScreen(self, string, type):
        if type == 'f':
            print('File: ' + string)
        elif type == 'd':
            print('Directory: ' + string)
        elif type == 'c':
            print('Comando: ' + string)
        elif type == 's':
            print(string)
    
    
    def addTextInFrame(self, text):
        leng = len(text)
        self.__class__.log += "\n" + text + "\n" + '-' * leng + "\n"
    
    def addCommand(self, command, h=True):
        self.printOnScreen(command, 'c')
        trash = open(os.devnull, 'w')  # file to put standard error
        if h:
            self.addTextInFrame('Command: ' + command)
        try:
            command1 = self.stripOptions(command)       # raw command (without options/pipe)
            if shutil.which(command1) is not None:      # command exists?
                
                # dmesg -l err or dmesg -l warn
                if command == 'dmesg -l err' or command == 'dmesg -l warn':         # dmesg -l {err, warn} only without systemd (SYSTEMD variable in 'constants' module)
                    if not constants.SYSTEMD:
                        out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)
                    else:
                        out=''
                
                # groups
                elif command == 'groups':
                    out = subprocess.check_output('su ' + constants.utente + ' -c ' + command, shell=True, universal_newlines=True, stderr=trash)
                    
                # iwconfig or iwlist scan - hide ESSID
                elif command == 'iwconfig' or command == 'iwlist scan':
                    out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)
                    out = re.sub('ESSID:.*', 'ESSID: *script removed*', str(out))
                   
                # all other commands
                else:
                    out = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=trash)

                # append output to the log
                self.__class__.log = ''.join((self.__class__.log,  str(out)))
                           
            else:
                self.__class__.log = ''.join((self.__class__.log,  'Comando non trovato\n'))
                
        except subprocess.CalledProcessError:
            pass
    
    def addFile(self, fileP):
        self.printOnScreen(fileP, 'f')
        self.addTextInFrame('File: ' + fileP)
        if self._ifFileExists(fileP):
            with open(fileP, 'r') as myfile:
                content = myfile.read()                                                         # file content in a variable
            
                # /var/log/syslog
                if fileP == '/var/log/syslog':
                    if not constants.SYSTEMD:                                                       # syslog only without systemd (SYTEMD variable in 'constants' module)
                        myre = re.compile('.*rsyslogd.*start')                                      # regular expression (RE)
                        try:
                            header = myre.findall(content)[-1]                                      # search the last occurence [-1] of previous RE
                            string1 = myre.split(content)[-1]                                       # last block (from 'header' to the end of file)
                            string2=''                                                              # syslog.1 not considered
                            
                        except IndexError:                                                          # RE can't match anything    
                            with open('/var/log/syslog.1', 'r') as myfile2:                         # open syslog.1 
                                content2 = myfile2.read()                                           # syslog.1 content in a variable
                                header = myre.findall(content2)[-1]             
                                string2 = myre.split(content2)[-1]
                                string1 = content                                                   #string1 contains entire syslog
                             
                        self.__class__.log = ''.join((self.__class__.log, header, string2, string1))    # join four strings
                
                # /etc/network/interfaces - hide ESSID/passphrase
                elif fileP == '/etc/network/interfaces':
                    content = re.sub('wpa-ssid.*', 'wpa-ssid *script removed*', content)
                    content = re.sub('wpa-psk.*', 'wpa-psk *script removed*', content)
                    
                    self.__class__.log = ''.join((self.__class__.log, content))
                
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
        self.addCommand('service "%s" status' % (deamon), False)
        
    def externalPackages(self):
        self.printOnScreen('Pacchetti esterni', 's')
        self.addTextInFrame('Pacchetti esterni')
        
        # variable that contains "apt-cache policy" output
        aptcachepol = str(subprocess.check_output('apt-cache policy', shell=True, universal_newlines=True))

        # extract release(s) and remove duplicates
        release = set((re.findall('(?<=n=)(.*?)(?=,)', aptcachepol, flags=re.MULTILINE)))

        # remove lines that are not in constants.releases
        release = filter(lambda rel: rel in constants.releases, release)
        
        # set-to-list conversion
        release = list(release)
        
        # list length - number of elements 
        num = len(release)
        
        if num == 1:
            if release[0] == constants.stable:
                output = str(subprocess.check_output("aptitude -F '%p %v %t' search '~S ~i !~Astable' --disable-columns | column -t", shell=True, universal_newlines=True))
            elif release[0] == constants.testing:
                output = str(subprocess.check_output("aptitude -F '%p %v %t' search '~S ~i !~Atesting' --disable-columns | column -t", shell=True, universal_newlines=True))
            elif release[0] == 'sid':
                output = str(subprocess.check_output("aptitude -F '%p %v %t' search '~S ~i !~Aunstable' --disable-columns | column -t", shell=True, universal_newlines=True))
            else:
                output = 'Release non gestita'
            
        elif num == 0:
            output = 'ERRORE! Nessuna release trovata.'
        
        else:
            output = 'Sono state trovate ' + str(num) + ' release.'
            
        # append output to the log
        self.__class__.log = ''.join((self.__class__.log, output))
                
    
    def getLogFile(self):
        return self.__class__.log
