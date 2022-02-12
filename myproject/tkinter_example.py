#import tkinter module
from tkinter import *

#make a tkinter window instance Tk()
window = Tk()

#givin the window a title
window.title("E6B Virtual Flight Computer")

#defining the size of the window
window.geometry("700x500")

#defining a minmun and max width and height of the window (width, height)
window.minsize(600,500)
window.maxsize(600,500)

#giving the window a color
window.config(bg="lightblue")

#creating a label

label1 = Label(window, text="Hello, guys!", bg="black", fg="white", \
    font=("Comic Sans", 25, "bold"), borderwidth=20, relief="groove")
label1.pack(anchor="e") 

#put the window in a loop until the close button is pressed
window.mainloop()