import sys, traceback

realo=sys.modules["__builtin__"].open
realf=sys.modules["__builtin__"].file

def fakeo(name, mode='r',buffering=0):
    print("File-system is being accessed from: %s" % sys._getframe())
    return realo(name, mode, buffering)

def fakef(name, mode='r',buffering=0):
    print("File-system is being accessed from: %s" % sys._getframe())
    return realf(name, mode, buffering)
    
sys.modules["__builtin__"].open=fakeo
sys.modules["__builtin__"].file=fakef
