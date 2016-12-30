import Tkinter as tkint
import threading
import Queue

q=Queue.Queue()
rq=Queue.Queue()

global root
root=None

def put(func, **kwargs):
    q.put((func, kwargs))

def loop():
    #global root
    if not q.empty():
        el=q.get()
        if len(el)>1:
            rq.put(el[0](**el[1]))
        else:
            rq.put(el[0]())

    root.after(1000, loop)

def strt():
    global root
    root=tkint.Tk()
    loop()
    root.mainloop()    

t=threading.Thread(target=strt,args=())
t.start()
        



