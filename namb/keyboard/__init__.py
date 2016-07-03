import namb.ui_processor

_DICT={}

def setup():
    import json, os
    f=open(os.path.join(__path__[0], "config.json"))
    global _DICT
    _DICT = json.load(f)
    f.close()

def bind(root):
    global _DICT
    for i in _DICT.keys():
        print(i)
        print(_DICT[i])
        root.bind(i, lambda e, z=i: namb.ui_processor.process(_DICT[z]))
    
def save():
    import os
    f=open(os.path.join(__path__[0], "config.json"),'w')
    f.write(json.dumps(_DICT))
    f.close()
