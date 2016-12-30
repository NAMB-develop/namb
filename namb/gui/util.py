
import Tkinter as tkint
from PIL.FontFile import WIDTH

class DebugLoadingScreen(object):
    
    def __init__(self, master):
        self.frame=tkint.Frame(master.frame, bg="black")
        self.frame.place(x=master.width/4,y=master.height/4,width=master.width/2, height=master.height/2)
        self.canvas=tkint.Canvas(self.frame, highlightthickness=0, bg="black")
        self.canvas.place(x=0,y=0,width=master.width/2, height=master.height/2)
        self.canvas.create_text(master.width/100, master.height/4, anchor=tkint.W, text="", fill="white", font=("Verdana", 12), tags="text")

    def set_message(self, message):
        self.canvas.itemconfig("text",text=message)
        
        
class SplashScreen(object):

    def __init__(self, master):
        import namb.gui
        self.width=namb.gui.width
        self.height=namb.gui.height
        self.frame=tkint.Frame(master, bg="black")
        self.frame.place(x=0,y=0,width=self.width, height=self.height)



class List(object):

    def __init__(self, parent, colors={"bg":"#0f0f0f","even":"#5f5f5f","odd":"#4f4f4f","selected":"#9f9f9f"}):
        
        self.colors=colors
        
        self.temp_started=0
        self.parentclass =parent
        self.pwidth=self.parentclass.width
        self.pheight=self.parentclass.height
        self.width=self.pwidth
        self.height=self.pheight
        self.stop=[True]
        self.items = None
        self.parent = parent.frame
        self.pframe=tkint.Frame(self.parent, bg=self.colors["bg"])
        self.pframe.place(x=0,y=self.pheight/10,width=self.pwidth,height=int(((self.pheight/10.0)*9))-(self.pheight/30))
        self.frame = tkint.Frame(self.pframe, bg=self.colors["bg"])
        self.frame.place(x=0,y=0,width=self.pwidth,height=int(((self.pheight/10.0)*9)))
        self.at=0

    def focus_receive(self):
        self.activate(self.at)

    def receive(self, event):
        import namb.userinput.keys
        import namb.userinput
        if event==namb.userinput.keys.UP:
            self.shift(-1)
        elif event==namb.userinput.keys.DOWN:
            self.shift(1)
        elif event==namb.userinput.keys.ENTER:
            self.select()
        elif event==namb.userinput.keys.BACK:
            self.deactivate(self.at)
            namb.userinput.set_receiver(self.parentclass.tabs)
            self.parentclass.focus_receive(self.__class__.name)
        elif event=="test":
            self.shiftshift()

    def select(self):
        self.frame.after(1, lambda: self.items[self.at][1]['callback'][0](*self.items[self.at][1]['callback'][1:]))
        #raise NotImplementedError("")

    def schedule(self, delay=1, *task):
        self.frame.after(delay, lambda: task[0](*task[1:]))

    def populate(self, items):
        self.items = []
        for i in items:
            self.items.append((tkint.Canvas(self.frame, bg=self.colors["even"], highlightthickness=0), i))
        self.frame.place(height=int((self.pheight/15)*(len(items)+1)))
        index=-1
        offset=self.pheight/30
        for i in self.items:
            index=index+1
            i[0].config(bg=self.colors["even"] if index%2==0 else self.colors["odd"])
            i[0].place(x=0,y=offset+(index*(self.pheight/15)), width=self.pwidth, height=self.pheight/15)
            i[0].create_text(self.pwidth/30,self.pheight/30,anchor=tkint.W, text=i[1]["name"],fill="white", font=("Verdana", 18))
            #i[0].create_text(width/2,height/30,text=i[1]["name"],fill="white", font=("Verdana", 18))

        self.update(0)

    def activate(self, item):
        self.items[item][0].config(bg=self.colors["selected"])

    def deactivate(self, item):
        self.items[item][0].config(bg=self.colors["even"] if item%2==0 else self.colors["odd"])

    def update(self, posneg):
        prev=self.at
        cur=self.at+posneg
        self.deactivate(prev)
        self.activate(cur)
        self.at=self.at+posneg

    def clear(self):
        self.items = None

    def shift(self, posneg):
        p=posneg #*-1
        if p+self.at<0 or p+self.at==len(self.items):
            return

        if self.items[p+self.at][0].winfo_y()+self.frame.winfo_y()>(self.pheight/10.0)*8 or self.items[p+self.at][0].winfo_y()+self.frame.winfo_y()<self.pheight/30:
            offset=posneg*(self.pheight/15)*-1
            self.frame.place(y=self.frame.winfo_y()+offset)

        self.update(p)
        
from datetime import datetime
        
class Player(object):

    def __init__(self, parent):
        self.parent = parent

        width=parent.width
        height=parent.height
        
        self.pwidth=width
        self.pheight=height
        
        self.playerframe = tkint.Frame(self.parent, bg="#2f2f2f")
        self.playerframe.place(x=0,rely=.9,relwidth=1,relheight=.1)

        self.playbutton = tkint.Canvas(self.playerframe, bg="#2f2f2f", highlightthickness=0)
        self.playbutton.place(x=width/100, y=0, width=.1*height, height=.1*height)

        self.playbuttontriangle = self.playbutton.create_polygon([height/50,height/50,(height/10)-height/50,height/20,height/50,(height/10)-height/50], fill="gray")

        self.playbutton.tag_bind(self.playbuttontriangle, "<Enter>", lambda e: self.playbutton.itemconfig(self.playbuttontriangle, fill="white"))
        self.playbutton.tag_bind(self.playbuttontriangle, "<Leave>", lambda e: self.playbutton.itemconfig(self.playbuttontriangle, fill="gray"))
        self.playbutton.bind("<Enter>", lambda e: self.playbutton.config(background="#4f4f4f"))
        self.playbutton.bind("<Leave>", lambda e: self.playbutton.config(background="#2f2f2f"))

        self.stopbutton = tkint.Canvas(self.playerframe, bg="#2f2f2f", highlightthickness=0)
        self.stopbutton.place(x=(width/50)+(height/10), y=0, width=height/10, height=height/10)

        self.stopbuttonsquare = self.stopbutton.create_polygon([height/50,height/50, (height/10)-(height/50), height/50, (height/10)-(height/50), (height/10)-(height/50), height/50, (height/10)-(height/50)], fill="gray")
            
        self.stopbutton.tag_bind(self.stopbuttonsquare, "<Enter>", lambda e: self.stopbutton.itemconfig(self.stopbuttonsquare, fill="white"))
        self.stopbutton.tag_bind(self.stopbuttonsquare, "<Leave>", lambda e: self.stopbutton.itemconfig(self.stopbuttonsquare, fill="gray"))
        self.stopbutton.bind("<Enter>", lambda e: self.stopbutton.config(background="#4f4f4f"))
        self.stopbutton.bind("<Leave>", lambda e: self.stopbutton.config(background="#2f2f2f"))

        self.playing = tkint.Canvas(self.playerframe, bg="#4f4f4f", highlightthickness=0)
        self.playing.place(x=(width/50)+(height/5)+(width/100), y=height/100, width=.85*width, height=(height/25)-(height/100))

        self.playingtext = self.playing.create_text(height/100, height/100, anchor=tkint.W, text="Lorem ipsum    -    Artists name", fill="white", font=("Verdana", 12))


        self.timebar = tkint.Canvas(self.playerframe, bg="#1f1f1f", highlightthickness=0,bd=0)
        self.timebar.place(x=(width/50)+(height/5)+(width/100), y=(height/100)+(height/25), width=.85*width, height=(height/25)-(height/100))

        self.currentloctext=self.timebar.create_text(.85*width,((height/25)-(height/100))/2, anchor=tkint.E, text="0:00", fill="white")

        self.currentloc = self.timebar.create_polygon([0,0,(.85*width)/2,0,(.85*width)/2, (height/25)-(height/100),0,(height/25)-(height/100)], fill="gray")
        
            
    def set_tracker(self, *callback):
        self.callback=callback
            
    def stop(self):
        self.state=False
        self.playbutton.config(background="#2f2f2f")
            
    def play(self):
        self.state=True
        self.playbutton.config(background="#4f4f4f")
        
        def loop():
            
            info=self.callback[0](*self.callback[1:])
            
            self.playingtext.config(text=info["artist"]+" - "+["title"])
            
            self.timebar.itemconfig(self.currentloctext,text=str((datetime.now()-info["start"])).split(".")[0])
            
            ratio=datetime.now()/float((info["stop"]-info["start"]).total_seconds())
            
            self.timebar.delete(self.currentloc)
            self.currentloc = self.timebar.create_polygon([0,0,(ratio*self.pwdith)/2,0,(ratio*self.pwdith)/2, (self.pheight/25)-(self.pheight/100),0,(self.pheight/25)-(self.pheight/100)], fill="gray")
            
            self.checkback=int((info["stop"]-datetime.now()).total_seconds())
            if self.checkback < 0:
                self.checkback=0.001
            
            if self.state:
                self.playerframe.after(self.checkback*1000, loop)
        
        self.playerframe.after(1, loop)
        