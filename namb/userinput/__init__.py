import Queue
_QUEUE=Queue.Queue()

_RECEIVER=None

def set_receiver(receiver):
    global _RECEIVER
    _RECEIVER=receiver

def get_receiver():
    global _RECEIVER
    return _RECEIVER

def queue(key):
    global _QUEUE
    _QUEUE.put(key)

def process_next(block=False):
    global _QUEUE
    if not _QUEUE.empty():
        process(_QUEUE.get(block))

def process(key):
    #print("Processed event: " + key)
    _RECEIVER.receive(key)
