import Xlib
from Xlib.display import Display

display = Display()

screen = display.screen()
w = screen.root.create_window(0, 0, 100, 100, 1,  screen.root_depth, event_mask = Xlib.X.KeyPressMask)
w.map()

while True:
    event = display.next_event()
    if event.type != Xlib.X.KeyPress:
        continue
    print "OHAI"
