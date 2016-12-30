import namb.userinput

_DICT={}

def setup():
    if _DICT:
        return
    import json, os
    f=open(os.path.join(__path__[0], "config.json"))
    global _DICT
    _DICT = json.load(f)
    f.close()

def bind(root):
    global _DICT
    for i in _DICT.keys():
        root.bind(i, lambda e, z=i: namb.userinput.queue(_DICT[z]))
    
def save():
    import os
    f=open(os.path.join(__path__[0], "config.json"),'w')
    f.write(json.dumps(_DICT))
    f.close()
