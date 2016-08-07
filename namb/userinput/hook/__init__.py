import sys

H=None

if 'linux' in sys.platform:
    import pyxhook as H
elif 'win' in sys.platform:
    import pyHook as H
    import pythoncom

import namb.userinput

_DICT={}

def setup():
    import json, os
    f=open(os.path.join(__path__[0], "hook.conf"))
    global _DICT
    _DICT = json.load(f)
    f.close()
    
def save():
    import os, json
    f=open(os.path.join(__path__[0], "hook.conf"),'w')
    f.write(json.dumps(_DICT))
    f.close()

def get(event):
    global _DICT
    if event.Key in _DICT:
        if event.WindowProcName in ["vlc","tk"]:
            namb.userinput.queue(_DICT[event.Key])

def hookup():
    if 'linux' in sys.platform:
        _hookup_linux()
    elif 'win' in sys.platform:
        _hookup_windows()

def _hookup_linux():
    global manager
    manager=H.HookManager()
    manager.KeyDown = get
    #manager.HookKeyboard()
    manager.start()

def _hookup_windows():
    global manager    
    manager=H.HookManager()
    manager.KeyDown = get
    manager.HookKeyboard()
    import threading
    global stopper
    stopper=threading.Event()
    thread=threading.Thread(target=_win_loop, args=())
    thread.daemon=True
    thread.start()
        
def _win_loop():
    while not stopper.is_set():
        pythoncom.PumpWaitingMessages()

def release():
    if 'linux' in sys.platform:
        manager.cancel()
    elif 'win' in sys.platform:
        global stopper
        stopper.set()
        manager.UnhookKeyboard()

