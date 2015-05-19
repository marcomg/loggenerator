# class for problem specific commands

import time
import loggenerator

class problem():
    
    def __init__(self):
        myloggenerator = loggenerator.functions()
            
    def commandsAPT(self):
        myloggenerator.addCommand('dpkg --print-architecture')
        myloggenerator.addCommand('apt-get update')
        myloggenerator.addCommand('apt-get -s -y upgrade')
        myloggenerator.addCommand('apt-get -s -y dist-upgrade')
        myloggenerator.addCommand('apt-get -s -y -f install')
        myloggenerator.addCommand('apt-get -s -y autoremove')
        myloggenerator.addCommand('apt-config dump')
        myloggenerator.addFile('/etc/apt/apt.conf')
        myloggenerator.addDir('/etc/apt/apt.conf.d/')
        myloggenerator.addFile('/etc/apt/preferences')
        myloggenerator.addDir('/etc/apt/preferences.d/')
        
        
    def commandsCommon(self):
        myloggenerator.addTextInFrame('Log creato ' + time.ctime())
        myloggenerator.addTextInFrame('Produttore:')
        myloggenerator.addFile('/sys/class/dmi/id/sys_vendor')
        myloggenerator.addTextInFrame('Prodotto')
        myloggenerator.addFile('/sys/class/dmi/id/product_name')
        myloggenerator.addTextInFrame('Versione')
        myloggenerator.addFile('/sys/class/dmi/id/product_version')
        myloggenerator.addTextInFrame('BIOS version')
        myloggenerator.addFile('/sys/class/dmi/id/bios_version')
        myloggenerator.addCommand('uname -a')
        myloggenerator.addFile('/etc/debian_version')
        # de_wm
        myloggenerator.addCommand('kde4-config --version')
        myloggenerator.addCommand('gnome-shell --version')
        myloggenerator.addCommand('xfce4-about | head -n1 | cut -d " " -f2')
        myloggenerator.addFile('/etc/X11/default-display-manager')
        myloggenerator.addCommand('groups')
        myloggenerator.addFile('/var/log/syslog')
        myloggenerator.addCommand('dmesg -l err')
        myloggenerator.addCommand('dmesg -l warn')
        myloggenerator.addCommand('lsmod')
        myloggenerator.addCommand('lspci -knn')
        myloggenerator.addCommand('lsusb')
        myloggenerator.addFile('/etc/apt/sources.list')
        myloggenerator.addDir('/etc/apt/sources.list.d/')
        myloggenerator.addCommand('fdisk -l')
        myloggenerator.addCommand('mount')
        myloggenerator.addCommand('df')
        myloggenerator.addCommand('apt-cache policy')
        myloggenerator.addCommand('apt-cache stats')
        myloggenerator.addCommand('apt-get check')
        # firmware
        myloggenerator.addDirList('/usr/lib/firmware')
        myloggenerator.addDirList('/usr/local/lib/firmware')
        myloggenerator.addDirList('/lib/firmware')
        myloggenerator.addDirList('/run/udev/firmware-missing')
        
    def commandsNetwork(self):
        myloggenerator.addFile('/etc/network/interfaces')
        myloggenerator.addFile('/etc/hosts')
        myloggenerator.addCommand('ifconfig')
        myloggenerator.addCommand('ifconfig -a')
        myloggenerator.addCommand('rfkill list all')
        myloggenerator.addCommand('ping -c3 8.8.8.8')  # DNS di Google 8.8.8.8
        myloggenerator.addCommand('ip addr')
        myloggenerator.addCommand('ip route list')
        myloggenerator.addCommand('iwconfig')
        myloggenerator.addCommand('iwlist scan')
        myloggenerator.addCommand('route -n')
        myloggenerator.isPackageInstalled('resolvconf')
        myloggenerator.addFile('/etc/resolv.conf')
        myloggenerator.isPackageInstalled('DHCP')
        myloggenerator.addFile('/etc/dhclient.conf')
        myloggenerator.isDeamonRunning('network-manager')
        myloggenerator.isDeamonRunning('wicd')
        
    def commandsVideo(self):
        myloggenerator.addFile('/etc/X11/xorg.conf')
        myloggenerator.addDir('/etc/X11/xorg.conf.d/')
        myloggenerator.addFile('/var/log/Xorg.0.log')
        myloggenerator.addCommand('dkms status')
        myloggenerator.isPackageInstalled('xserver-xorg')
        myloggenerator.isPackageInstalled('nouveau')
        myloggenerator.isPackageInstalled('nvidia')
        myloggenerator.isPackageInstalled('mesa')
        myloggenerator.isPackageInstalled('fglrx')
        
    def commandsMount(self):
        myloggenerator.addCommand('udisks --dump')
        myloggenerator.isPackageInstalled('usbmount')

    def commandsTouchpad(self):
        myloggenerator.isPackageInstalled('xserver-xorg')
        myloggenerator.isPackageInstalled('touchpad')
        myloggenerator.addFile('/etc/X11/xorg.conf')
        myloggenerator.addDir('/etc/X11/xorg.conf.d/')
        myloggenerator.addFile('/var/log/Xorg.0.log')
        myloggenerator.addCommand('/usr/bin/synclient -l')
    
        
