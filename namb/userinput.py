RECEIVER=None

def set_receiver(receiver):
    global RECEIVER
    RECEIVER=receiver

def get_receiver():
    global RECEIVER
    return RECEIVER

def event(key):
    print("Processed event: " + key)
    RECEIVER.receive(key)
