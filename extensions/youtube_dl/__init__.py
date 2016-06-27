NAME="youtube_dl"
VERSION="0.1"
NAMB_VERSION="0.1"
EXTENSION_DEPENDENCIES=[]
MODULE=None

import zipfile
import urllib2
import os
import importlib
import StringIO

def is_prepared():
    return os.path.isdir(__path__[0]+os.sep+"youtube_dl")

def remove():
    os.remove(__path__[0]+os.sep+"youtube_dl")

def prepare():
    response = urllib2.urlopen('https://github.com/rg3/youtube-dl/archive/master.zip') #TODO: Implement versioning
    zipcontent = response.read()
    s=StringIO.StringIO(zipcontent)
    try:
        z=zipfile.ZipFile(s,'r')
    except zipfile.BadZipfile:
        print("Zip extraction failed!")
        raise
    
    l=z.namelist()

    for i in z.filelist:
        if '/youtube_dl/' in i.filename:
            if i.filename.split('/youtube_dl/')[1]:
                i.filename='youtube_dl/' + i.filename.split('/youtube_dl/')[1]

    for i in l:
        if '/youtube_dl/' in i:
            if i.split('/youtube_dl/')[1]:
                z.extract(i, __path__[0])

    z.close()
##    response = urllib2.urlopen('https://github.com/rg3/youtube-dl/archive/master.zip')
##    zipcontent= response.read()
##
##    with open(__path__[0]+os.sep+"ydl.zip",'wb') as f:
##            f.write(zipcontent)
##
##    z = zipfile.ZipFile(__path__[0]+os.sep+'ydl.zip','r')
##    zz=zipfile.ZipFile(__path__[0]+os.sep+'youtube_dl.zip','w')
##
##    for member in z.namelist():
##            if '/youtube_dl/' in member:
##                    if member.split('/youtube_dl/')[1]:
##                            zz.writestr('youtube_dl/'+member.split('/youtube_dl/')[1], z.read(member))
##
##    
##    zz.extractall(__path__[0])
##
##    zz.close()
##    z.close()
##
##    os.remove(__path__[0]+os.sep+'ydl.zip')
##    os.remove(__path__[0]+os.sep+'youtube_dl.zip')

def load():
    global MODULE
    MODULE=importlib.import_module("extensions.youtube_dl."+"youtube_dl")
    return MODULE
