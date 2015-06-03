# class for problem specific commands

import time
import loggenerator
import simpleprompt
import os

class problem():
    
    def __init__(self):
        self.myloggenerator = loggenerator.functions()
            
    def commandsAPT(self):
        self.myloggenerator.addCommand('dpkg --print-architecture')
        self.myloggenerator.addCommand('apt-get update')
        self.myloggenerator.addCommand('apt-get -s -y upgrade')
        self.myloggenerator.addCommand('apt-get -s -y dist-upgrade')
        self.myloggenerator.addCommand('apt-get -s -y -f install')
        self.myloggenerator.addCommand('apt-get -s -y autoremove')
        self.myloggenerator.addCommand('apt-config dump')
        self.myloggenerator.addFile('/etc/apt/apt.conf')
        self.myloggenerator.addDir('/etc/apt/apt.conf.d/')
        self.myloggenerator.addFile('/etc/apt/preferences')
        self.myloggenerator.addDir('/etc/apt/preferences.d/')
        
        
    def commandsCommon(self):
        self.myloggenerator.addTextInFrame('Log creato ' + time.ctime())
        self.myloggenerator.addTextInFrame('Produttore:')
        self.myloggenerator.addFile('/sys/class/dmi/id/sys_vendor')
        self.myloggenerator.addTextInFrame('Prodotto')
        self.myloggenerator.addFile('/sys/class/dmi/id/product_name')
        self.myloggenerator.addTextInFrame('Versione')
        self.myloggenerator.addFile('/sys/class/dmi/id/product_version')
        self.myloggenerator.addTextInFrame('BIOS version')
        self.myloggenerator.addFile('/sys/class/dmi/id/bios_version')
        self.myloggenerator.addCommand('uname -a')
        self.myloggenerator.addFile('/etc/debian_version')
        # de_wm
        self.myloggenerator.addCommand('kde4-config --version')
        self.myloggenerator.addCommand('gnome-shell --version')
        self.myloggenerator.addCommand('xfce4-about | head -n1 | cut -d " " -f2')
        self.myloggenerator.addFile('/etc/X11/default-display-manager')
        self.myloggenerator.addCommand('groups')
        self.myloggenerator.addCommand('systemctl --failed')
        self.myloggenerator.addCommand('journalctl -x -b --no-pager') 
        self.myloggenerator.addCommand('journalctl -x -b --no-pager -p err')
        self.myloggenerator.addCommand('journalctl -x -b --no-pager -p warning')
        self.myloggenerator.addCommand('systemd-delta')
        self.myloggenerator.addCommand('systemd-cgtop --no-pager')
        self.myloggenerator.addCommand('systemd-cgls --no-pager')
        self.myloggenerator.addFile('/var/log/syslog')
        self.myloggenerator.addCommand('dmesg -l err')
        self.myloggenerator.addCommand('dmesg -l warn')
        self.myloggenerator.addCommand('lsmod')
        self.myloggenerator.addCommand('lspci -knn')
        self.myloggenerator.addCommand('lsusb')
        self.myloggenerator.addFile('/etc/apt/sources.list')
        self.myloggenerator.addDir('/etc/apt/sources.list.d/')
        self.myloggenerator.addCommand('fdisk -l')
        self.myloggenerator.addCommand('mount')
        self.myloggenerator.addCommand('df')
        self.myloggenerator.addCommand('apt-cache policy')
        self.myloggenerator.addCommand('apt-cache stats')
        self.myloggenerator.addCommand('apt-get check')
        # firmware
        self.myloggenerator.addDirList('/usr/lib/firmware')
        self.myloggenerator.addDirList('/usr/local/lib/firmware')
        self.myloggenerator.addDirList('/lib/firmware')
        self.myloggenerator.addDirList('/run/udev/firmware-missing')
        self.myloggenerator.externalPackages()
        
    def commandsNetwork(self):
        self.myloggenerator.addFile('/etc/network/interfaces')
        self.myloggenerator.addFile('/etc/hosts')
        self.myloggenerator.addCommand('ifconfig')
        self.myloggenerator.addCommand('ifconfig -a')
        self.myloggenerator.addCommand('rfkill list all')
        self.myloggenerator.addCommand('ping -c3 8.8.8.8')  # DNS di Google 8.8.8.8
        self.myloggenerator.addCommand('ip addr')
        self.myloggenerator.addCommand('ip route list')
        self.myloggenerator.addCommand('iwconfig')
        self.myloggenerator.addCommand('iwlist scan')
        self.myloggenerator.addCommand('route -n')
        self.myloggenerator.isPackageInstalled('resolvconf')
        self.myloggenerator.addFile('/etc/resolv.conf')
        self.myloggenerator.isPackageInstalled('DHCP')
        self.myloggenerator.addFile('/etc/dhclient.conf')
        self.myloggenerator.isDeamonRunning('network-manager')
        self.myloggenerator.isDeamonRunning('wicd')
        
    def commandsVideo(self):
        self.myloggenerator.addFile('/etc/X11/xorg.conf')
        self.myloggenerator.addDir('/etc/X11/xorg.conf.d/')
        self.myloggenerator.addFile('/var/log/Xorg.0.log')
        self.myloggenerator.addCommand('dkms status')
        self.myloggenerator.isPackageInstalled('xserver-xorg')
        self.myloggenerator.isPackageInstalled('nouveau')
        self.myloggenerator.isPackageInstalled('nvidia')
        self.myloggenerator.isPackageInstalled('mesa')
        self.myloggenerator.isPackageInstalled('fglrx')
        
    def commandsMount(self):
        self.myloggenerator.addCommand('udisks --dump')
        self.myloggenerator.isPackageInstalled('usbmount')

    def commandsTouchpad(self):
        self.myloggenerator.isPackageInstalled('xserver-xorg')
        self.myloggenerator.isPackageInstalled('touchpad')
        self.myloggenerator.addFile('/etc/X11/xorg.conf')
        self.myloggenerator.addDir('/etc/X11/xorg.conf.d/')
        self.myloggenerator.addFile('/var/log/Xorg.0.log')
        self.myloggenerator.addCommand('/usr/bin/synclient -l')
        
    def commandsAudio(self):
        self.myloggenerator.isPackageInstalled('alsa')
        self.myloggenerator.isPackageInstalled('pulseaudio')
        
        alsaurl = 'http://www.alsa-project.org/alsa-info.sh'
        print('''I log relativi ai problemi audio sono ricavati attraverso lo script di debug ALSA prelevabile all'indirizzo: ''' + alsaurl)
        if simpleprompt.boolQuestionY('Verrà ora scaricato e eseguito lo script ALSA. Continuare?'):
            try:
                os.remove('alsa-info.sh')
            except FileNotFoundError:
                pass
            os.system('wget -q ' + alsaurl)
            os.chmod('alsa-info.sh', 777)
            print('Esecuzione script')
            self.myloggenerator.addCommand('./alsa-info.sh --stdout')
            os.remove('alsa-info.sh')
    
        
