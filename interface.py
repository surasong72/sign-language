import tkinter as tk
#from tkinter import ttk
from tkinter import * 
from tkinter import Canvas
from PIL import Image, ImageTk
import cv2
# this is the function called when the button is clicked
def btnClickFunction():
	root.destroy()
	cap.release()



root = Tk()

# This is the section of code which creates the main window
root.geometry('720x600')
root.configure(background='#C1CDCD')
root.title('\u121D\u120D\u12AD\u1275 \u124B\u1295\u124B')

frame_parent=Frame(root, width=700,height=600)
frame_parent.grid(column=0,row=0)

frame_top=Frame(frame_parent, width=80,height=100)
frame_top.grid(column=0, row=0)

# This is the section of code which creates the a label
Label(frame_top, bg='#B9F3FC',text='\u12E8\u12A0\u121B\u122D\u129B \u121D\u120D\u12AD\u1275 \u124B\u1295\u124B \u1218\u121B\u122A\u12EB', height=4,width=50,font=('courier', 19, 'bold')).grid(row=0, column=0)

frame_middle=Frame(frame_parent, width=700,height=200,bg="yellow")
frame_middle.grid(column=0,row=1,padx=30,pady=20)

frame_pic=Frame(frame_middle,width=200,height=200)
frame_pic.grid(column=0,row=0,padx=50,pady=50)

label=Label(frame_pic).grid(column=0,row=0,padx=40,pady=40)

image = Image.open("C:\\Users\\sures\\Downloads\\sign.jpg")
        # Resize the image using resize() method
resize_image = image.resize((300, 200))
img = ImageTk.PhotoImage(resize_image)
        # create label and add resize image
label = Label(image=img)
label.image = img

cap=cv2.VideoCapture(0)

frame_button=Frame(frame_middle,width=80,height=100,bg="purple")
frame_button.grid(column=1,row=1,pady=30,padx=30)

def capture():
        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        #cv2image.resize(400,450)
        cv2.flip(cv2image,1)
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(img)
        label.imgtk= imgtk
        label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        label.after(20, capture)
        
# This is the section of code which creates a button
button_start=Button(frame_button, text='\u1300\u121D\u122D', height=2,width=8,bg='light cyan', font=('courier', 19, 'bold'), command=capture)
button_start.grid(column=1,row=0)


# This is the section of code which creates a button
button_stop=Button(frame_button, text='\u12A0\u1241\u121D ',height=2,width=8, bg='light cyan', font=('courier', 19,'bold'),command=btnClickFunction)
button_stop.grid(column=1,row=1)

frame_bottom=Frame(frame_parent,width=300,height=200)
frame_bottom.grid(column=0,row=2)


button_display=Button(frame_bottom, text='test',state=DISABLED, height=2,width=20,bg='light cyan', font=('courier', 19, 'bold'))
button_display.grid(column=0,row=0,columnspan=2)
#output=Text(root, height=5, width=35, bg=("light cyan")).place(x=45, y=386)
#photo = PhotoImage(file = 'gesture.jpg')
#root.iconphoto(False, photo)

root.resizable(False,False)
root.mainloop()
