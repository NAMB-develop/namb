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
    response = urllib2.urlopen("https://github.com/NAMB-develop/jazzradio_com/archive/master.zip")
    zipcontent = response.read()
    s=StringIO.StringIO()
    s.write(zipcontent)
    z=zipfile.ZipFile(s,'r')

    ss=StringIO.StringIO()
    zz=zipfile.ZipFile(ss,'w')
    for member in z.namelist():
        if member.split('jazzradio_com-master/')[1]:
            zz.writestr('jazzradio_com/'+member.split('jazzradio_com-master/')[1])

    zz.extractall(__path__[0])
    zz.close()
    z.close()

def load():
    MODULE=importlib.import_module("plugins.jazzradio_com.jazzradio_com")
    return MODULE
