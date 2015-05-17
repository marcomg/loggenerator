# class for handling standard operations against a file

import os
import loggenerator

class FileOps():
    
    def __init__(self, filename):
        self.filename = filename
        self.f = ''
        
    def open(self):
        self.f = open(self.filename, 'w')
        
    def write(self):
        self.f.write(loggenerator.getLogFile())
        
    def close(self):
        self.f.close
    
    # Set permissions to 666
    def chmod(self):
        os.chmod(self.filename, 666)
        
    def go(self):
        self.open()
        self.write()
        self.close()
        self.chmod()
        
        
