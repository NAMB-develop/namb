_extensions_path_list=[]
_extensions={}
headers={}

import os
import importlib

def load():
    init()
    load_extensions_headers()

def init():
    l = [os.path.join(__path__[0], i) for i in os.listdir(__path__[0])]
    ll = [i for i in l if os.path.isdir(i)]
    global _extensions_path_list
    _extensions_path_list=ll
    return _extensions_path_list

def load_extensions_headers():
    for e in _extensions_path_list:
        name = e.split(os.sep)[-1]
        m=importlib.import_module("extensions."+name)
        headers[m.NAME]=m
    return headers

def install_plugin(name):
    if headers[name].is_installed():
        return
    return headers[name].install()
    
def is_installed(name):
    return headers[name].is_installed()

def load_extension(name):
    import main
    if compare_versions(main.NAMB_VERSION, headers[name].NAMB_VERSION) > -1:
        if not headers[name].is_installed():
            raise Exception("Extension not installed")
            #headers[name].install()
        _extensions[name]=headers[name].load()
        return _extensions[name]!=None
    else:
        raise Exception("Version of extension not supported.")

def get_extension(name):
    return _extensions[name] if name in _extensions else None

def is_loaded(name):
    return name in _extensions

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
    
    
