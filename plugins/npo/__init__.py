NAME="npo"
DEPENDENCIES=["vlc","youtube_dl"]
VERSION="0.1"
NAMB_VERSION="0.1"
MODULE=None

import importlib

def is_prepared():
    return True

def prepare():
    pass

def load():
    MODULE=importlib.import_module("plugins.npo.npo")
    return MODULE
