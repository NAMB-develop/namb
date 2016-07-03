import namb.ui_processor as ui_proc
import lirc

_INTERPR={}

def setup():
    import json, os
    lirc.setconfigfile("lirc.conf")
    global _INTERPR
    f=open(os.path.join(__path__[0], "config.json"))
    _INTERPR = json.load(f)
    f.close()
    


def loop():
    while True:
        do()


def do():
    global _INTERPR
    raw = lirc.readnext()
    if raw in _INTERPR:
        ui_proc.process(_INTERPR[raw])
