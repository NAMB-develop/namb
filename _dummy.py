#Just for path stuff
import json

#Temp
import extensions
extensions.load_extension("vlc")
import plugins
plugins.load_plugin("jazzradio_com")
plugins.get_plugin("jazzradio_com").init()
channels=plugins.get_plugin("jazzradio_com").plugin.load_channels()
plugins.get_plugin("jazzradio_com").plugin.initialize_dict()
print(plugins.get_plugin("jazzradio_com").plugin.get_currently_playing_channel('mellowpianojazz'))
j=plugins.get_plugin("jazzradio_com").plugin
