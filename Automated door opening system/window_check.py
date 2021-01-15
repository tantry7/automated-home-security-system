from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('600x600')
root.title("ALLOWER WINDOW")


text = Label (root,text="ALLOW THE PERSON INSIDE")
text.pack()

photo = PhotoImage(file="image.png")
labelphoto = Label(root,image = photo)

labelphoto.pack()
result = messagebox.askyesno(message='Do you want to allow this person')
if not result:
    exit()
root.mainloop()
exit()
