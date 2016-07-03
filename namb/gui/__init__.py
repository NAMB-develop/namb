import sys
if sys.version_info[0] > 2:
    import tkinter as tkint
else:
    import Tkinter as tkint

global fullscreen
fullscreen=False

global root
root=None



class LoadingButton(object):

    def __init__(self):
        pass

class PluginScreenContainer(object):

    def __init__(self):
        self.frame = tkint.Frame(root, bg='black')
        self.q = .95
        self.marg = 8

    def appear(self):
        self.frame.place(anchor=tkint.CENTER, relx=.5, rely=.5, relwidth=(width-(2*self.marg))/width, relheight=(height-(2*self.marg))/height)

class Bar(object):

    def closebuttonclick(self, event=None):
        print("Closebutton was clicked.")
        self.barframe.master.destroy()

    def settingsbuttonclick(self, event=None):
        print("Settingsbutton was clicked.")
        raise NotImplemented("Oops.")

    def receive(self, key):
        import namb.keys
        if key==namb.keys.ENTER:
            if self.focus[1]==0:
                if self.focus[0]==1:
                    self.closebuttonclick()
                elif self.focus[0]==0:
                    self.settingsbuttonclick()
        if key==namb.keys.LEFT:
            self.focus[0]=self.focus[0]-1 if self.focus[0]>0 else 0

    def __init__(self):
        self.focus=(1,0)
        import namb.ui_processor as userinput
        import namb.keys
        userinput.set_receiver(self)

        self.animationspeed=5
        self.animationincrement=5

        self.buttons=[]
        
        self.barframe = tkint.Frame(root, bg='pink')
        self.barframe.place(relx=0, rely=0.89, relwidth=1, relheight=0.1)
        self.canvas = tkint.Canvas(self.barframe, bg="#002430", highlightthickness=0, bd=1)
        self.canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        self._color1 = "#003242"
        self._color2 = "#002430"
        self.canvas.bind("<Configure>", self._draw_gradient)

        self.closebuttonframe = tkint.Frame(root, bg='pink')
        self.closebuttonframe.place(relx=1-.025, rely=0, relwidth=.025, relheight=.025*(width/(height+0.0)))
        self.closebuttoncanvas = tkint.Canvas(self.closebuttonframe, bg="#003242",highlightthickness=0, bd=1)
        self.closebuttoncanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        def _draw_cross(event=None):
            self.closebuttoncanvas.delete("lines")
            self.closebuttoncanvas.create_line(self.closebuttonframe.winfo_width()/5, self.closebuttonframe.winfo_height()/5, self.closebuttonframe.winfo_width()-(self.closebuttonframe.winfo_width()/5), self.closebuttonframe.winfo_height()-(self.closebuttonframe.winfo_height()/5), width=4, fill="gray", tags=("lines",))
            self.closebuttoncanvas.create_line(self.closebuttonframe.winfo_width()/5, self.closebuttonframe.winfo_height()-(self.closebuttonframe.winfo_height()/5), self.closebuttonframe.winfo_width()-(self.closebuttonframe.winfo_width()/5), self.closebuttonframe.winfo_height()/5, width=4, fill="gray", tags=("lines",))        
        self.closebuttoncanvas.bind("<Configure>", _draw_cross)

        self.settingsbuttonframe = tkint.Frame(root, bg='pink')
        self.settingsbuttonframe.place(relx=1-0.055, rely=0, relwidth=.025, relheight=.025*(width/(height+0.0)))
        self.settingsbuttoncanvas = tkint.Canvas(self.settingsbuttonframe, bg="#003242", highlightthickness=0, bd=1)
        self.settingsbuttoncanvas.place(relx=0,rely=0,relwidth=1,relheight=1)

        def _draw_circle(event=None):
            self.settingsbuttoncanvas.delete("lines")
            self.settingsbuttoncanvas.create_rectangle(self.settingsbuttonframe.winfo_width()/5, self.settingsbuttonframe.winfo_height()/5, self.closebuttonframe.winfo_width()-(self.closebuttonframe.winfo_width()/5), self.closebuttonframe.winfo_height()-(self.closebuttonframe.winfo_height()/5), width=4, outline="gray", tags=("lines",))
        self.settingsbuttoncanvas.bind("<Configure>", _draw_circle)
        
        def do():
            userinput.process(namb.keys.ENTER)

        #self.barframe.after(2000, do)
        
    def menu_vanish(self):
        self.disappear()
        self.cross_disappear()

    def menu_appear(self):
        self.appear()
        self.cross_appear()

    def appear(self):
        def animate(event = None):
            if self.barframe.winfo_y()/(height+0.0) > .89:
                self.barframe.place(relx=0, rely=((self.barframe.winfo_y()-self.animationincrement)/height))
                self.barframe.after(self.animationspeed, animate)
        self.barframe.after(self.animationspeed, animate)

    def disappear(self):
        def animate(event = None):
            if self.barframe.winfo_y()/(height+0.0) < 1:
                self.barframe.place(relx=0, rely=((self.barframe.winfo_y()+self.animationincrement)/height))
                self.barframe.after(self.animationspeed, animate)
        self.barframe.after(self.animationspeed, animate)

    def cross_appear(self):
        def animate(event = None):
            if self.closebuttonframe.winfo_y() < 0:
                self.closebuttonframe.place(rely=(self.closebuttonframe.winfo_y()+self.animationincrement)/height)
                self.settingsbuttonframe.place(rely=(self.closebuttonframe.winfo_y()+self.animationincrement)/height)
                self.closebuttonframe.after(self.animationspeed, animate)
        self.closebuttonframe.after(self.animationspeed, animate)

    def cross_disappear(self):
        def animate(event = None):
            if self.closebuttonframe.winfo_y() >= 1-self.closebuttonframe.winfo_height():
                self.closebuttonframe.place(rely=(self.closebuttonframe.winfo_y()-self.animationincrement)/height)
                self.settingsbuttonframe.place(rely=(self.closebuttonframe.winfo_y()-self.animationincrement)/height)
                self.closebuttonframe.after(self.animationspeed, animate)
        self.closebuttonframe.after(self.animationspeed, animate)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.canvas.delete("gradient")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        limit = height/3
        (r1,g1,b1) = self.canvas.winfo_rgb(self._color1)
        (r2,g2,b2) = self.canvas.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            #self.canvas.create_line(i,0,i,height, tags=("gradient",), fill=color)
            self.canvas.create_line(0,i,width,i , tags=("gradient",), fill=color)
        self.canvas.lower("gradient")  

class MainWindow(object):
    
    def __init__(self):
        global root
        root=tkint.Tk()
        global width, height
        width=1280.0
        height=720.0
        if fullscreen:
            width=float(root.winfo_screenwidth())
            height=float(root.winfo_screenheight())
            root.overrideredirect(1)
        root.bind("<Escape>", lambda e: root.destroy())
        root.geometry("%dx%d+0+0" % (width, height))
        root.focus_set()
        
        self.mainframe = tkint.Frame(root, bg='black')
        self.mainframe.place(x=0, y=0, relwidth=1, relheight=1)

        self.backgroundcanvas = tkint.Canvas(self.mainframe, bg='#4d4d4d', highlightthickness=0)
        self.backgroundcanvas.place(x=0, y=0, relwidth=1, relheight=1)
        global backgroundcanvas
        backgroundcanvas =  self.backgroundcanvas
        self._color1 = "#4d4d4d"
        self._color2 = "#1d1d1d"
        #self.backgroundcanvas.bind("<Configure>", self._draw_gradient)
        
        self.loadingcanvas = tkint.Canvas(self.mainframe,bg='gray',highlightthickness=0, bd=1)
        self.loadingcanvas.place(anchor=tkint.CENTER, relx=0.5,rely=0.5,relwidth=0.25,relheight=0.05)

        def create_bar(event=None):
            self.loadingcanvas.create_rectangle(0,0,self.loadingcanvas.winfo_width()/3, self.loadingcanvas.winfo_height(), fill="#008FBF",outline="#008FBF")

        self.loadingcanvas.bind("<Configure>", create_bar)

        self.p = PluginScreenContainer()

        self.bar=Bar()
        self.loadingcanvas.destroy()

        self.p.appear()


    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.backgroundcanvas.delete("gradient")
        width = self.backgroundcanvas.winfo_width()
        height = self.backgroundcanvas.winfo_height()
        limit = width
        (r1,g1,b1) = self.backgroundcanvas.winfo_rgb(self._color1)
        (r2,g2,b2) = self.backgroundcanvas.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.backgroundcanvas.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.backgroundcanvas.lower("gradient")        
        
        
    def display(self):
        root.mainloop()

if __name__=="__main__":
    print("Running in GUI debug mode.")
    import os
    sys.path.insert(0, os.path.join(sys.path[0],'..','..'))
    m=MainWindow()
    m.display()
    
