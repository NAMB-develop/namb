from simplejson.tests import test_namedtuple
from __main__ import name
_plugins_path_list=[]
_plugins={}
headers={}

import os
import importlib

_filehandles={}

import namb.files

class FileHandle(object):

    def __init__(self, pluginname):
        _filehandles[pluginname]=self
        self.__path=os.path.join(__path__[0], "..", ".settings", pluginname)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def get_file_handle(self, *path):
        if "." in path or ".." in path:
            raise Exception("Illegal to traverse out of path!")
            return None
        dirs=path[:-1]
        if dirs:
            os.makedirs(os.path.join(*dirs))
        p=os.path.join(dirs)
        return namb.files.file_handle(p, 'a+')

def load():
    init()
    load_plugins_headers()

def init():
    l = [os.path.join(__path__[0], i) for i in os.listdir(__path__[0])]
    ll = [i for i in l if os.path.isdir(i)]
    global _plugins_path_list
    _plugins_path_list=ll
    return _plugins_path_list

def load_plugins_headers():
    for e in _plugins_path_list:
        name = e.split(os.sep)[-1]
        m=importlib.import_module("plugins."+name)
        headers[m.NAME]=m
    return headers

def install_plugin(name):
    if headers[name].is_installed():
        return
    return headers[name].install()
    
def is_installed(name):
    return headers[name].is_installed()

def load_plugin(name):
    import main
    if compare_versions(main.NAMB_VERSION, headers[name].NAMB_VERSION) > -1:
        import extensions
        for i in headers[name].DEPENDENCIES:
            if i not in extensions.headers:
                raise Exception("Dependency not satisfied: %s" % (i))
        if not headers[name].is_installed():
            raise Exception("Plugin not installed")
            #headers[name].install()
        _plugins[name]=headers[name].load()
        return _plugins[name]!=None
    else:
        raise Exception("Version of plugin not supported.")

def get_plugin(name):
    return _plugins[name] if name in _plugins else None

def is_loaded(name):
    return name in _plugins

def compare_versions(v1, v2):
    v1_splitted=tuple(int(i) for i in v1.split("."))
    v2_splitted=tuple(int(i) for i in v2.split("."))
    if v1_splitted == v2_splitted:
        return 0
    elif v1_splitted > v2_splitted:
        return 1
    elif v1_splitted < v2_splitted:
        return -1
    else:
        raise Exception("Version checking failed for versions: %s and %s" % (v1, v2))
        return -99
    
    
