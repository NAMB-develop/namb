
import Tkinter as tkint

class DebugLoadingScreen(object):
    
    def __init__(self, master):
        self.frame=tkint.Frame(master, bg="black")
        self.frame.place(x=master.winfo_width()/4,y=master.winfo_height()/4,width=master.winfo_width()/2, height=master.winfo_height()/2)
        self.canvas=tkint.Canvas(self.frame, highlightthickness=0, bg="black")
        self.canvas.place(x=0,y=0,width=master.winfo_width()/2, height=master.winfo_height()/2)
        self.canvas.create_text(master.winfo_width()/100, master.winfo_height()/4, anchor=tkint.W, text="", fill="white", font=("Verdana", 12), tags="text")

    def set_message(self, message):
        self.canvas.itemconfig("text",text=message)
        
        
