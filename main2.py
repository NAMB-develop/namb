NAMB_VERSION="0.1"
NAMB_VERSIONp=(0,1)

import sys
import plugins
import extensions


#Routine is this:
#import extensions
#import plugins
#check necessary extensions for the plugins
#Load extensions
#Load plugins

#The main thread should be displaying a loading screen.



def fetch_todo():
    
    def todo_plugin(name):
        todo=[]
        if plugins.is_installed(name):
            for dep in plugins.headers[name].DEPENDENCIES:
                if extensions.is_installed(dep):
                    todo.append(dep)
                else:
                    return []
            return (todo,name)
        return []
    
    extensions.load()
    plugins.load()
    ext_req=[]
    plugs=[]
    for name in plugins.headers.keys():
        for i in todo_plugin(name):
            ext_req.append(i[0])
            plugs.append(i[1])
        
    todo=[(extensions.load_extension, ext[0]) for ext in ext_req]
            
    for plug in plugs:
        todo.append((plugins.load_plugin, plug))
        
    return todo
            

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

    loadscreen=namb.gui.util.DebugLoadingScreen(splash)
    
    import namb.util
    w=namb.util.Worker()
    
    
    todo=fetch_todo()
    for tod in todo:
        w.submit(*tod)
    print("Loading jobs submitted")
    
    w.start()
    w.is_alive()
    
    
    print("Entering mainloop")
    namb.gui.root.mainloop()
    
    import Queue
    
load()