import tkinter as tk
import pywinstyles as pws
import random
import PIL
from PIL import Image, ImageOps, ImageTk

root = tk.Tk("Dvd logo test")
root.geometry("600x500")

root.configure(bg="black")
pws.change_border_color(root, color="black")
pws.change_header_color(root, color="black")
pws.change_title_color(root, color="white")
w, h = (100, 100)

img = Image.open("logo.png").resize((w, h), Image.Resampling.LANCZOS)
tkImg = ImageTk.PhotoImage(img)

clrs = ["blue", "purple", "pink", "orange", "green", "red", "cyan"]
currentColor = "blue"

canvas = tk.Canvas(width=root.winfo_width(), height=root.winfo_height(), bg="black", border=0, borderwidth=0, highlightbackground="black", highlightcolor="black")
canvas.pack()

logo = canvas.create_image(w/2, h/2, image=tkImg)

speed = 2
tickMs = 13 # amount of milliseconds for a tick to pass (change the logo's pos)
allowRecolor = True
Debugging = False

#the config is a bit buggy here cuz of the position structure diffrences between create_image and create_rectangle


direction = [speed, speed]


lastImm = 0
fTime = True
imm = False
dTicks = 0

def ChangeColor():
    if allowRecolor:
        global currentColor
        global clrs
        global img
        global tkImg


        tempArr = []
        for i in clrs:
            tempArr.append(i)
        tempArr.remove(currentColor)

        currentColor = random.choice(tempArr)
        tempImg = ImageOps.colorize(img.convert("L"), black="black", white=currentColor)
        tkImg = ImageTk.PhotoImage(tempImg)
        canvas.itemconfigure(logo, image=tkImg)
    


cProp = [w, h]
def Update():
    global lastImm
    global imm
    global fTime
    global cProp

    canvas.configure(width=root.winfo_width(), height=root.winfo_height())

    coords = canvas.coords(logo)
    x, y = (coords[0]+w/2, coords[1]+h/2) # the +w/2 and +y/2 is cuz the canvas.coords() for create_image is only x and y (the center basically) but the recrangle one's is x1, y1, x2, y2 and x2 and y2 were used there 
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
