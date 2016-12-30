def pr(e):
    print(e)

import pyxhook as H
manager=H.HookManager()
manager.KeyDown = pr
#manager.HookKeyboard()
manager.start()
