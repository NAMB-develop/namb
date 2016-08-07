NAMB_VERSION="0.1"

import sys


#Load order:
#Load plugin headers. Load extension headers. Check plugin dependencies. Check extension availability. Add plugins to list, but do not initialize all, only when clicked or requested to prevent long loading times.
#Loading time should only consist of graphics creation.

if __name__=="__main__":

    import namb.gui as gui
    
    m=gui.MainWindow()

    import timeit
    import extensions
    import plugins

    extensions.load_extension("vlc")
    extensions.load_extension("youtube_dl")
    plugins.load_plugin("npo")
    npo=plugins.get_plugin("npo")
    npo.init()
    npo.display(m.p.frame)
    #jazzradio_com.display(m.p.frame)
    
    m.display()
