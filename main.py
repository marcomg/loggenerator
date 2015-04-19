#!/usr/bin/python3
# Standard library
import sys
import os
import getpass
import time

# Personal library
sys.path.append('libs') # questa linea solo se non pacchettizato
import programStrings
import pastedebian
import simpleprompt
import loggenerator
import fileHandler

# Intro
print(programStrings.programIntroString)

# Chiedo conferma
print(programStrings.programAdviceStrings)
if not simpleprompt.boolQuestionY('Continuare?'):
    exit()

# Controllo di essere root
#if getpass.getuser() != 'root':
#    print('Lo script deve essere lanciato da root.')
#    exit()

# Seleziono il tipo di problema
problem = simpleprompt.multiChoose(programStrings.menuItemsStrings,
                                   len(programStrings.menuItemsStrings),
                                   programStrings.menuItemsQuestion)

# Genero i log
# 0 esci
if problem == 0:
    exit()
    
# 7 commons (da eseguire sempre tranne che allo 0) e altro tipo di problemi
if problem in [1, (len(programStrings.menuItemsStrings))-1]:
    loggenerator.addTextInFrame('Log creato ' + time.ctime())
    loggenerator.addTextInFrame('Produttore:')
    loggenerator.addFile('/sys/class/dmi/id/sys_vendor')
    loggenerator.addTextInFrame('Prodotto')
    loggenerator.addFile('/sys/class/dmi/id/product_name')
    loggenerator.addTextInFrame('Versione')
    loggenerator.addFile('/sys/class/dmi/id/product_version')
    loggenerator.addTextInFrame('BIOS version')
    loggenerator.addFile('/sys/class/dmi/id/bios_version')
    loggenerator.addCommand('/bin/uname -a')
    loggenerator.addFile('/etc/debian_version')
    #de_wm
    loggenerator.addCommand('kde4-config --version')
    loggenerator.addCommand('gnome-shell --version')
    loggenerator.addCommand('xfce4-about | head -n1 | cut -d " " -f2')
    loggenerator.addFile('/etc/X11/default-display-manager')
    loggenerator.addCommand('/usr/bin/groups')
    loggenerator.addFile('/var/log/syslog')
    loggenerator.addCommand('/bin/dmesg -l err')
    loggenerator.addCommand('/bin/dmesg -l warn')
    loggenerator.addCommand('/bin/lsmod')
    loggenerator.addCommand('/usr/bin/lspci -knn')
    loggenerator.addCommand('/usr/bin/lsusb')
    loggenerator.addFile('/etc/apt/sources.list')
    loggenerator.addDir('/etc/apt/sources.list.d/')
    loggenerator.addCommand('/sbin/fdisk -l')
    loggenerator.addCommand('/bin/mount')
    loggenerator.addCommand('/bin/df')
    loggenerator.addCommand('/usr/bin/apt-cache policy')
    loggenerator.addCommand('/usr/bin/apt-cache stats')
    loggenerator.addCommand('/usr/bin/apt-get check')
    # firmware
    loggenerator.addDirList('/usr/lib/firmware')
    loggenerator.addDirList('/usr/local/lib/firmware')
    loggenerator.addDirList('/lib/firmware')
    loggenerator.addDirList('/run/udev/firmware-missing')
    ## _extpack #TODO non fatto in quanto metodo da migliorare
# 1 problemi relativi alle connessioni di rete
if problem == 1:
    loggenerator.addFile('/etc/network/interfaces')
    loggenerator.addFile('/etc/hosts')
    loggenerator.addCommand('/sbin/ifconfig')
    loggenerator.addCommand('/sbin/ifconfig -a')
    loggenerator.addCommand('/usr/sbin/rfkill list all')
    loggenerator.addCommand('/bin/ping -c3 8.8.8.8') #DNS di Google 8.8.8.8
    loggenerator.addCommand('/bin/ip addr')
    loggenerator.addCommand('/bin/ip route list')
    loggenerator.addCommand('/sbin/iwconfig')
    loggenerator.addCommand('/sbin/iwlist scan')
    loggenerator.addCommand('/sbin/route -n')
    loggenerator.isPackageInstalled('resolvconf')
    loggenerator.addFile('/etc/resolv.conf')
    loggenerator.isPackageInstalled('DHCP')
    loggenerator.addFile('/etc/dhclient.conf')
    loggenerator.isDeamonRunning('network-manager')
    loggenerator.isDeamonRunning('wicd')
# 2 problemi video
elif problem == 2:
    loggenerator.addFile('/etc/X11/xorg.conf')
    loggenerator.addDir('/etc/X11/xorg.conf.d/')
    loggenerator.addFile('/var/log/Xorg.0.log')
    loggenerator.addCommand('/usr/sbin/dkms status')
    loggenerator.isPackageInstalled('xserver-xorg')
    loggenerator.isPackageInstalled('nouveau')
    loggenerator.isPackageInstalled('nvidia')
    loggenerator.isPackageInstalled('mesa')
    loggenerator.isPackageInstalled('fglrx')
# 3 problemi audio
elif problem == 3:
    loggenerator.isPackageInstalled('alsa')
    alsaurl = 'http://www.alsa-project.org/alsa-info.sh'
    print('''I log relativi ai problemi audio sono ricavati attraverso lo script di debug
ALSA prelevabile all'indirizzo: ''' + alsaurl)
    if simpleprompt.boolQuestionY('Verrà ora scaricato e eseguito lo script ALSA. Continuare?'):
        try:
            os.remove('alsa-info.sh')
        except FileNotFoundError:
            pass
        os.system('wget ' + alsaurl)
        os.chmod('alsa-info.sh', 777)
        print('Esecuzione script')
        loggenerator.addCommand('./alsa-info.sh --stdout')
        os.remove('alsa-info.sh')
# 4 problemi di gestione dei pacchetti (APT)
elif problem == 4:
    loggenerator.addCommand('/usr/bin/dpkg --print-architecture')
    loggenerator.addCommand('/usr/bin/apt-get update')
    loggenerator.addCommand('/usr/bin/apt-get -s -y upgrade')
    loggenerator.addCommand('/usr/bin/apt-get -s -y dist-upgrade')
    loggenerator.addCommand('/usr/bin/apt-get -s -y -f install')
    loggenerator.addCommand('/usr/bin/apt-get -s -y autoremove')
    loggenerator.addCommand('/usr/bin/apt-config dump')
    loggenerator.addFile('/etc/apt/apt.conf')
    loggenerator.addDir('/etc/apt/apt.conf.d/')
    loggenerator.addFile('/etc/apt/preferences')
    loggenerator.addDir('/etc/apt/preferences.d/')
# 5 problemi di mount/unmount
elif problem == 5:
    loggenerator.addCommand('/usr/bin/udisks --dump')
    loggenerator.isPackageInstalled('usbmount')
# 6 problemi di funzionamento del touchpad
elif problem == 6:
    loggenerator.isPackageInstalled('xserver-xorg')
    loggenerator.isPackageInstalled('touchpad')
    loggenerator.addFile('/etc/X11/xorg.conf')
    loggenerator.addDir('/etc/X11/xorg.conf.d/')
    loggenerator.addFile('/var/log/Xorg.0.log')
    loggenerator.addCommand('/usr/bin/synclient -l')


# Log file name based on the current date
fileLogName = 'log-' + time.strftime("%d%m%Y-%H%M%S")

# myfile is an object of the class "fileOps" in fileHandler(.py) module
myfile = fileHandler.fileOps(fileLogName)
myfile.go()

# Invio i logs a paste.debian.net
if simpleprompt.boolQuestion('Vuoi inviare i logs su paste.debian.net?'):
    print('Invio in corso, attendere...')
    links = []
    f = open(fileLogName, 'r')
    while True:
        tmp = f.readlines(100 * 1024) # 100 KiB
        tmp = ''.join(tmp)
        if tmp == '':
            break
        else:
            links.append(pastedebian.addPaste(tmp, expire = 60*60*24*30)['view_url'])# i links scadono dopo un mese
    print('invio completato. I links sono:')
    for link in links:
        print(link)