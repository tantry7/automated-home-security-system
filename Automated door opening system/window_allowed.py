from tkinter import *
from tkinter import messagebox
from OCR_allow import *

root = Tk()
root.geometry('600x600')
root.title("ALLOWER WINDOW")


text = Label (root,text=str(Name)+ " IS ALLOWED INSIDE")
text.pack()

photo = PhotoImage(file="image.png")
labelphoto = Label(root,image = photo)
labelphoto.pack()
root.mainloop()
exit()
