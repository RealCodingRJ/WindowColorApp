import random

from GeoMaths import Geo
from tkinter import *

from Sizable import Resize

window = Tk()
window.title("| Window of Random Colors |")
geo = Geo(1200, 1200)

rValue = random.randint(2, 255)
gValue = random.randint(2, 255)
bValue = random.randint(2, 255)

top = Frame(window, bg="red")

l = Label(top,text=f"R: {rValue}",   height=5)
l2 = Label(top, text=f"G: {gValue}", height=5)
l3 = Label(top, text=f"B: {bValue}", height=5)
l.config(font=("Sans-seif", 20), bg="red")
l2.config(font=("Sans-seif", 20), bg="red")
l3.config(font=("Sans-seif", 20), bg="red")

top.pack(fill="none", pady=5, padx=70)

l.pack()
l2.pack()
l3.pack()

window.geometry(f"{int(geo.getX())}x{int(geo.getY())}")
window.configure(background="red")
sizeable = Resize(False, False)



window.resizable(sizeable.getRightOption(), sizeable.getLeftOption())
window.mainloop()

