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
    import plugins
    global g
    g=plugins.get_plugin("jazzradio_com")
    g.init()
    g.display(m.p.frame)
    import namb.userinput
    namb.userinput.set_receiver(g.menu_frame.tabs)
    g.menu_frame.tabs.focus_receive()
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
    splash=namb.gui.util.SplashScreen(namb.gui.root)

    loadscreen=namb.gui.util.DebugLoadingScreen(splash.frame)

    global lst
    lst=["extensions","plugins","plugins_step2"]
    namb.gui.root.after(1, load_routine)
    namb.gui.root.mainloop()

def loop(running, get):
    if running():
        import namb.gui
        namb.gui.root.after(10, lambda: loop(running, get))
    else:
        a=get()
        import namb.gui
        namb.gui.root.after(10, lambda: load_routine())

def thread():
    import threading
    t=threading.Thread(target=load)
    t.start()

def load_routine():

    def nxt():
        import namb.gui
        namb.gui.root.after(10, lambda: load_routine())
    
    global lst
    print("Load routine: %s"%lst)
    import namb.util
    if lst:
        q=lst[0]
        lst=lst[1:]
        if q=="extensions":
            print("Importing extensions")
            import importlib
            #import extensions
            namb.util.call_while_waiting_for(loop, importlib.import_module, "extensions")
            print("Done")
        elif q=="plugins":
            print("Importing plugins")
            import importlib
            #import plugins
            namb.util.call_while_waiting_for(loop, importlib.import_module, "plugins")
        elif q=="plugins_step2":
            print("Appending based on plugins")
            import plugins
            for p in plugins.headers.values():
                for dep in p.DEPENDENCIES:
                    lst.insert(0, "extension_"+dep)
            for p in plugins.headers.keys():
                lst.append("plugin_"+p)
            print("Done")
            nxt()
        elif q.startswith("extension_"):
            print("Loading extension")
            import extensions
            ext=q.split("extension_")[1]
            if not extensions.is_loaded(ext):
                namb.util.call_while_waiting_for(loop, extensions.load_extension, ext)
            nxt()
            print("Done")
        elif q.startswith("plugin_"):
            print("Loading plugin")
            import plugins
            plu=q.split("plugin_")[1]
            if not plugins.is_loaded(plu):
                namb.util.call_while_waiting_for(loop, plugins.load_plugin, plu)
            if not lst:
                lst.append("done")
            nxt()
            print("Done")
        elif q.startswith("done"):
            print("Done loading!")
            start()            
            
    

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
