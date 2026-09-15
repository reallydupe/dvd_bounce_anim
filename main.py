import tkinter as tk
import pywinstyles as pws
import random

root = tk.Tk("Dvd logo test")
root.geometry("600x500")

root.configure(bg="black")
pws.change_border_color(root, color="black")
pws.change_header_color(root, color="black")
pws.change_title_color(root, color="white")
w, h = (100, 100)

clrs = ["blue", "purple", "pink", "orange", "green", "red", "cyan"]
currentColor = "blue"

canvas = tk.Canvas(width=root.winfo_width(), height=root.winfo_height(), bg="black", border=0, borderwidth=0, highlightbackground="black", highlightcolor="black")
canvas.pack()

logo = canvas.create_rectangle(0, 0, w, h, fill="blue")

Debugging = False

speed = 2
tickMs = 13 # amount of milliseconds for a tick to pass (change the logo's pos)

direction = [speed, speed]

lastImm = 0
fTime = True
imm = False
dTicks = 0

def ChangeColor():
    global currentColor
    global clrs

    tempArr = []
    for i in clrs:
        tempArr.append(i)
    tempArr.remove(currentColor)
    print(clrs)

    currentColor = random.choice(tempArr)
    canvas.itemconfigure(logo, fill=currentColor) 

cProp = [w, h]
def Update():
    global lastImm
    global imm
    global fTime
    global cProp

    canvas.configure(width=root.winfo_width(), height=root.winfo_height())

    coords = canvas.coords(logo)
    x, y = (coords[2], coords[3])
    dx, dy = (direction[0], direction[1])

    hx, hy = (x != root.winfo_width(), y != root.winfo_height()) 

    cw, cy = (cProp[0], cProp[1])
    ihx, ihy = (x != cw, y != cy) 

    if ((hx and hy) and (ihx and ihy)) or imm == True:
        imm = False
        #print("MV", imm, hx, hy, ihx, ihy, hx and hy)
        canvas.move(logo, dx, dy)
    else:

        if fTime == True:
            ihx = ihy = True
            if x > 100:
                fTime = False
        if hx == False or ihx == False:
            direction[0] = -direction[0]
            ChangeColor()
        if hy == False or ihy == False:
            direction[1] = -direction[1]
            ChangeColor()
        imm = True
        if Debugging: print("[DEBUG] direction change (direction. hit x, hit y)", direction, hx, hy)


    root.after(tickMs, Update)

Update()

root.mainloop()
