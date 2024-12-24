import requests
import random
import tkintertools as tkt
import json
from datetime import datetime
import tkinter.messagebox as messagebox
import pywinstyles
from PIL import Image, ImageTk
import tkinter as tk

def ask() -> None:
    if messagebox.askyesno(message="是否关闭窗口？"):
        root.destroy()

window_width = 550
window_height = 300
size = 550, 300
root = tkt.Tk(title="linecap-doodle", size=size)
root.center()

# 加载背景图片
image_path = "1.jpg"  # 替换为你的图片路径
image = Image.open(image_path)

# 缩放图片以完全填充窗口（强制填充，避免白边）
image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)

# 将图片转换为Tkinter可以使用的格式
background_image = ImageTk.PhotoImage(image)
# 创建Label并设置图片
label = tk.Label(root, image=background_image)
label.place(relwidth=1, relheight=1)  # 让Label填充整个窗口

root.resizable(False, False)
pywinstyles.apply_style(root, "dark")
# 样式："dark", "mica", "aero", "transparent", "acrylic", "win7","inverse", "popup", "native", "optimised", "light"
root.shutdown(ask)
root.mainloop()

unfinished_tasks = []
