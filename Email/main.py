from tkinter import *#
from PIL import Image, ImageTk

print('Hello')

x = Tk()
image =  ImageTk.PhotoImage(file="C:/Users/nikit/OneDrive/Desktop/github/python/Email/a.jpg")
label = Label(x, image=image)
label.pack()
x.mainloop()