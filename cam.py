

# Import Module
from tkinter import *
from PIL import Image, ImageTk

# Create Tkinter Object
root = Tk()
root.title("this is a drill")
root.configure(bg="blue")
#root.geometry('600x700')
root.maxsize(900, 600)
#root.geometry(height=600, width=720)
frame_parent=Frame(root, bg='red', width=100,height=100)
frame_parent.grid(column=0,row=0)

frame_top=Frame(frame_parent,bg="yellow")
frame_top.grid(column=0,row=0)

Label(frame_top,text="hello try this").grid(column=0,row=0,pady=10,rowspan=2)

frame_two=Frame(frame_parent, height=100,width=100,bg="green")
frame_two.grid(column=0,row=1)

Label(frame_two,text="hi beloved").grid(column=0,row=0,padx=10,rowspan=2)

frame_side=Frame(frame_parent,width=70,height=100,bg="purple")
frame_side.grid(column=1,row=1)

Label(frame_side,text="hello world").grid(column=1,row=0,padx=10)

Label(frame_side,text="somebody come").grid(column=1,row=1,padx=10)

frame_bottom=Frame(frame_parent, height=100,width=100,bg="aqua")
frame_bottom.grid(column=0,row=2)

Label(frame_bottom,text="third row and column").grid(column=0,row=0,pady=10,padx=20)

# Execute Tkinter
root.mainloop()
