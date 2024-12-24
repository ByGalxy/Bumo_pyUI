import requests
import random
import tkintertools as tkt
import json
from datetime import datetime
import tkinter.messagebox as messagebox
import pywinstyles
import tkintertools.animation as animation
import tkintertools.core.configs as configs
import tkintertools.core.virtual as virtual


class MyToplevel(tkt.Toplevel):
    def __init__(self, *args, **kw) -> None:
        self.feature: virtual.Feature = None


configs.Env.system = "Windows11"


def ask() -> None:
    if messagebox.askyesno(message="是否关闭窗口？"):
        root.destroy()


size = size = 550, 300
root = tkt.Tk(title="linecap-doodle", size=size)
root.center()

# 0.0.1 设置不许缩放窗口
root.resizable(False, False)
pywinstyles.apply_style(root, "aero")
# 样式："dark", "mica", "aero", "transparent", "acrylic", "win7","inverse", "popup", "native", "optimised", "light"
root.shutdown(ask)

root.mainloop()
