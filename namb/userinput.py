INTERPRETER=None

def set_interpreter(interpreter):
    global INTERPRETER
    INTERPRETER=interpreter

def get_interpreter():
    global INTERPRETER
    return INTERPRETER

def event(key):
    print("Received event: " + key)
    INTERPRETER.interpret(key)
