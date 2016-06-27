NAME="npo"
DEPENDENCIES=["vlc","youtube_dl"]
VERSION="0.1"
NAMB_VERSION="0.1"
MODULE=None

import importlib, os

def is_prepared():
    return os.path.isdir(__path__[0]+os.sep+"npo")

def remove():
    os.remove(__path__[0]+os.sep+"npo")

def prepare():
    response = urllib2.urlopen("https://github.com/NAMB-develop/npo/archive/master.zip") #TODO: Implement versioning
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
    MODULE=importlib.import_module("plugins.npo.npo")
    return MODULE
