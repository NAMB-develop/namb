import namb.ui_processor as ui_proc

global _DICT
_DICT={}

def setup():

    import json, os
    f=open(os.path.join(__path__[0], "config.json"))
    _DICT = json.load(f)
    f.close()

def bind(root):
    for i in _DICT:
        root.bind(i, ui_proc.process(_DICT[i]))
    
