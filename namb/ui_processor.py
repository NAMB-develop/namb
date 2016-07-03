_RECEIVER=None

def set_receiver(receiver):
    global _RECEIVER
    _RECEIVER=receiver

def get_receiver():
    global _RECEIVER
    return _RECEIVER

def process(key):
    print("Processed event: " + key)
    _RECEIVER.receive(key)
