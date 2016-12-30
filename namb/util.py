
import threading, Queue

class Worker(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self.inqueue = Queue.Queue()
        self.outqueue = Queue.Queue()
        self.stopped = False
        self.daemon = True
        
    def stop(self):
        self.stopped = True
        self.inqueue.put(None)
        
    def submit(self, *task):
        self.inqueue.put(task)
        
    def run(self):
        while not self.stopped:
            task = self.inqueue.get()
            if task:
                try:
                    result=task[0](*task[1:])
                except Exception as e:
                    result=e
                self.outqueue.put(result)
        
        threading.Thread.join(self)
    

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
        
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            
    def join(self):
        threading.Thread.join(self)
        return self._return

def call_while_waiting_for(callback, *func):
    t=ThreadWithReturnValue(target=func[0],args=func[1:])
    #t.daemon=True
    t.start()

    def running():
        return t.is_alive()

    def get():
        return t.join()
    
    callback(running, get)
