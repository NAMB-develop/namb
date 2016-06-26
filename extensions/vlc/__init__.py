NAME="vlc"
VERSION="0.1"
NAMB_VERSION="0.1"
EXTENSION_DEPENDENCIES=[]
MODULE=None

import urllib2, os, importlib

path=os.path.join(__path__[0], "vlc")

def is_prepared():
    global path
    return os.path.isfile(path + os.sep + "generated_vlc.py")
    
def prepare():
    request = urllib2.urlopen("https://git.videolan.org/?p=vlc/bindings/python.git;a=blob_plain;f=generated/vlc.py;hb=HEAD")
    response = request.read()

    global path
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
    try:
        f=open(path+os.sep+"__init__.py","w")
        f.close()
    except OSError:
        raise
    with open(path+os.sep+"generated_vlc.py",'wb') as f:
        f.write(response)

def load():
    import os, sys
    VLC_PATH="X:\\My Documents\\Projects\\VLC"
    if sys.platform.startswith('win'):
        os.environ['PATH'] =  VLC_PATH + ';' + os.environ['PATH']
    global MODULE
    MODULE = importlib.import_module("extensions.vlc.vlc."+"generated_vlc")
    return MODULE
