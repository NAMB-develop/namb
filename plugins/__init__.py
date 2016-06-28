_plugins_path_list=[]
_plugins={}
headers={}

import os
import importlib

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

def load_plugin(name):
    import main
    if compare_versions(main.NAMB_VERSION, headers[name].NAMB_VERSION) > -1:
        import extensions
        for i in headers[name].DEPENDENCIES:
            if i not in extensions.headers:
                raise Exception("Dependency not satisfied: %s" % (i))
        if not headers[name].is_installed():
            headers[name].install()
        _plugins[name]=headers[name].load()
    else:
        raise Exception("Version of plugin not supported.")

def get_plugin(name):
    return _plugins[name] if name in _plugins else None

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
    
    

init()
load_plugins_headers()
