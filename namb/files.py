import sys, traceback

_DEBUG=False

_realo=sys.modules["__builtin__"].open
_realf=sys.modules["__builtin__"].file

def _fakeo(name, mode='r',buffering=0):
    _u()
    print("File-system is being accessed (open): %s" % traceback.format_exc())
    _s()
    return _realo(name, mode, buffering)

def _fakef(name, mode='r',buffering=0):
    _u()
    print("File-system is being accessed (file): %s" % traceback.format_exc())
    _s()
    return _realf(name, mode, buffering)

def _s():
    sys.modules["__builtin__"].open=_fakeo
    sys.modules["__builtin__"].file=_fakef

def _u():
    sys.modules["__builtin__"].open=_realo
    sys.modules["__builtin__"].file=_realf

if _DEBUG:
    _s()

def file_handle(name, mode='r', buffering=0):
    return _realo(name, mode, buffering)
