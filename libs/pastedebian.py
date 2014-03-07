#
# How use:
# import pastedebian
# # TO UPLOAD A PASTE
# pastedebian.addPaste('The text to insert', 'The name', 'When expire (an int)', 'TheLanguage', 'If hidden')
# (solo il primo argomento è obbligatorio)
# return a dictionary with download_url, delete_url, view_url, digest (the digest of the entry), id (the id number)
#
# # TO DELETE A PASTE


import xmlrpc.client

class PasteError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

protocol = 'http://'
url = 'http://paste.debian.net'
server = xmlrpc.client.ServerProxy('http://paste.debian.net/server.pl')

def addPaste(pastetext, name = '', expire = -1, lang = '', hidden = 0):
    result = server.paste.addPaste(pastetext, name, expire, lang, hidden)
    #print(result)
    # If there is an error
    if result['rc'] != 0:
        raise PasteError('There has been an error during the upload process :(, return status ' + str(result['rc']))
    else:
        return {'download_url':protocol + result['download_url'][2:], 'delete_url':protocol + result['delete_url'][2:], 'view_url':protocol + result['view_url'][2:], 'digest':result['digest'], 'id':result['id']}

def deletePaste(digest):
    result = server.paste.deletePaste(digest)
    if result['rc'] != 0:
        raise PasteError('There has been an error during the deleting process')
    else:
        return True

def getPaste(id):
    result = server.paste.getPaste(id)
    if result['rc'] != 0:
        raise PasteError('There has been an error during download paste')
    else:
        return {'code':result['code'], 'submitter':result['submitter'], 'submitdate':result['submitdate'], 'expiredate':result['expiredate']}

def getLanguages():
    result = server.paste.getLanguages()
    if result['rc'] != 0:
        raise PasteError('There has been an error during getting supported languages list')
    else:
        return result['langs']
