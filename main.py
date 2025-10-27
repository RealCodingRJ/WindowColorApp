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

l = Label(window, text=f"R: {rValue}")
l2 = Label(window, text=f"G: {gValue}")
l3 = Label(window, text=f"B: {bValue}")

l.config(font=("Sans-seif", 30))
l2.config(font=("Sans-seif", 30))
l3.config(font=("Sans-seif", 30))


window.geometry(f"{int(geo.getX())}x{int(geo.getY())}")
window.configure(background="red")
sizeable = Resize(False, False)

window.resizable(sizeable.getRightOption(), sizeable.getLeftOption())
window.mainloop()

