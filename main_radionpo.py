NAMB_VERSION="0.1"

import sys


#Load order:
#Load plugin headers. Load extension headers. Check plugin dependencies. Check extension availability. Add plugins to list, but do not initialize all, only when clicked or requested to prevent long loading times.
#Loading time should only consist of graphics creation.

def q():
    import namb.userinput.hook
    namb.userinput.hook.unhook()
    import namb.gui.root
    namb.gui.root()
    import namb.userinput.ui_server
    namb.userinput.ui_server.stop()

def ui_loop():
    import namb.gui
    import namb.userinput
    namb.userinput.process_next()
    namb.gui.root.after(10, ui_loop)

def start():
    import namb.gui as gui
    global m
    m=gui.MainWindow()
    import extensions
    extensions.load()
    extensions.load_extension("vlc")
    import plugins
    plugins.load()
    plugins.install_plugin("radionpo")
    plugins.load_plugin("radionpo")
    #plugins.load_plugin("jazzradio_com")
    global g
    g=plugins.get_plugin("radionpo")
    g.init()
    g.display(m.p.frame)
    import namb.userinput
    namb.userinput.set_receiver(g.menu)
    g.menu.focus_receive()
    m.p.frame.after(1, lambda: m.bar.menu_vanish())
    ui_loop()
    #m.display()

def load():
    import namb.userinput.hook
    namb.userinput.hook.setup()
    namb.userinput.hook.hookup()

    import namb.userinput.ui_server
    namb.userinput.ui_server.run()

    
    import namb.gui
    namb.gui.init_tk()
    
    import namb.gui.util

    namb.gui.root.after(1, start)

    namb.gui.root.mainloop()         
            
    

if __name__=="__main__":

    load()

    #import namb.gui.util

#    import namb.gui as gui
    
    #m=gui.MainWindow()
#
    #import extensions
#    import plugins

  #  import namb.gui.util
##    
##
##    extensions.load_extension("vlc")
##    extensions.load_extension("youtube_dl")
##    plugins.load_plugin("npo")
##    npo=plugins.get_plugin("npo")
##    npo.init()
##    npo.display(m.p.frame)
##    #jazzradio_com.display(m.p.frame)
##    
##    m.display()
