# class for problem specific commands

import time
import loggenerator

class problem():
    
            
    def commandsAPT(self):
        loggenerator.addCommand('dpkg --print-architecture')
        loggenerator.addCommand('apt-get update')
        loggenerator.addCommand('apt-get -s -y upgrade')
        loggenerator.addCommand('apt-get -s -y dist-upgrade')
        loggenerator.addCommand('apt-get -s -y -f install')
        loggenerator.addCommand('apt-get -s -y autoremove')
        loggenerator.addCommand('apt-config dump')
        loggenerator.addFile('/etc/apt/apt.conf')
        loggenerator.addDir('/etc/apt/apt.conf.d/')
        loggenerator.addFile('/etc/apt/preferences')
        loggenerator.addDir('/etc/apt/preferences.d/')
        
        
    def commandsCommon(self):
        loggenerator.addTextInFrame('Log creato ' + time.ctime())
        loggenerator.addTextInFrame('Produttore:')
        loggenerator.addFile('/sys/class/dmi/id/sys_vendor')
        loggenerator.addTextInFrame('Prodotto')
        loggenerator.addFile('/sys/class/dmi/id/product_name')
        loggenerator.addTextInFrame('Versione')
        loggenerator.addFile('/sys/class/dmi/id/product_version')
        loggenerator.addTextInFrame('BIOS version')
        loggenerator.addFile('/sys/class/dmi/id/bios_version')
        loggenerator.addCommand('uname -a')
        loggenerator.addFile('/etc/debian_version')
        # de_wm
        loggenerator.addCommand('kde4-config --version')
        loggenerator.addCommand('gnome-shell --version')
        loggenerator.addCommand('xfce4-about | head -n1 | cut -d " " -f2')
        loggenerator.addFile('/etc/X11/default-display-manager')
        loggenerator.addCommand('groups')
        loggenerator.addFile('/var/log/syslog')
        loggenerator.addCommand('dmesg -l err')
        loggenerator.addCommand('dmesg -l warn')
        loggenerator.addCommand('lsmod')
        loggenerator.addCommand('lspci -knn')
        loggenerator.addCommand('lsusb')
        loggenerator.addFile('/etc/apt/sources.list')
        loggenerator.addDir('/etc/apt/sources.list.d/')
        loggenerator.addCommand('fdisk -l')
        loggenerator.addCommand('mount')
        loggenerator.addCommand('df')
        loggenerator.addCommand('apt-cache policy')
        loggenerator.addCommand('apt-cache stats')
        loggenerator.addCommand('apt-get check')
        # firmware
        loggenerator.addDirList('/usr/lib/firmware')
        loggenerator.addDirList('/usr/local/lib/firmware')
        loggenerator.addDirList('/lib/firmware')
        loggenerator.addDirList('/run/udev/firmware-missing')
        # # _extpack #TODO non fatto in quanto metodo da migliorare
        
    
        
