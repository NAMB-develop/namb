NAME="jazzradio_com"
DEPENDENCIES=["vlc"]
VERSION="0.1"
NAMB_VERSION="0.1"
MODULE=None

import importlib

def is_prepared():
    return True

def prepare():
    pass

def load():
    MODULE=importlib.import_module("plugins.jazzradio_com.jazzradio_com")
    return MODULE
