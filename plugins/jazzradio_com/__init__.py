NAME="jazzradio_com"
DEPENDENCIES=["vlc"]
VERSION="0.1"
NAMB_VERSION="0.1"
MODULE=None

import importlib
import zipfile
import urllib2
import os
import StringIO

def is_prepared():
    return os.path.isdir(__path__[0]+os.sep+"jazzradio_com")

def remove():
    os.remove(__path__[0]+os.sep+"jazzradio_com")

#UNTESTED
def prepare():
    response = urllib2.urlopen("https://github.com/NAMB-develop/jazzradio_com/archive/master.zip") #TODO: Implement versioning
    zipcontent = response.read()
    s=StringIO.StringIO(zipcontent)
    try:
        z=zipfile.ZipFile(s,'r')
    except zipfile.BadZipfile:
        print("Zip extraction failed!")
        raise
    
    l=z.namelist()

    for i in z.filelist:
        i.filename=''.join(i.filename.split('-master'))

    for i in l:
        z.extract(i, __path__[0])

    z.close()

def load():
    MODULE=importlib.import_module("plugins.jazzradio_com.jazzradio_com")
    return MODULE
