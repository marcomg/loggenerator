# class for handling standard operations against a file

import os
import loggenerator
import constants
import re

class FileOps():
    
    def __init__(self, filename):
        self.filename = filename
        self.f = ''
        
    def open(self):
        self.f = open(self.filename, 'w')
        
    def write(self):
        self.f.write(self.hide())
        
    def close(self):
        self.f.close
    
    # Set permissions to 666
    def chmod(self):
        os.chmod(self.filename, 666)
        
    # hide away the username and hostname from log file
    # only whether username/hostname aren't in constants.passList list
    def hide(self):
        myloggenerator = loggenerator.functions()
        myvar = myloggenerator.getLogFile()
        
        if constants.utente not in constants.passList:
            myvar = re.sub(r'\b' + constants.utente + r'\b', 'nomeutente', myvar)
            
        if constants.nomehost not in constants.passList:
            myvar = re.sub(r'\b' + constants.nomehost + r'\b', 'nomehost', myvar)
            
        return myvar
        
    def go(self):
        self.open()
        self.write()
        self.close()
        self.chmod()
        
        
