import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2

def btnClickFunction():
	root.destroy()
	cap.release()

root=Tk()
root.title("\u121D\u120D\u12AD\u1275 \u124B\u1295\u124B")
root.configure(bg="light cyan")
root.maxsize(800,768)
root.geometry("800x768+270+0")

cap=cv2.VideoCapture(0)
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

frame_parent=Frame(root,width=300,height=80)
frame_parent.pack(side=tk.TOP)

label_title=Label(frame_parent,bg='#B9F3FC',
                  text='\u12E8\u12A0\u121B\u122D\u129B \u121D\u120D\u12AD\u1275 \u124B\u1295\u124B \u1218\u121B\u122A\u12EB',
                  height=4,width=60,font=('courier', 19, 'bold'))
label_title.pack()

frame_middle=Frame(root,width=200,height=300,bg='light cyan')
frame_middle.pack(side=tk.RIGHT)

button_start=Button(frame_middle, text='\u1300\u121D\u122D',
                    height=2,width=8,bg='#84D2C5',
                    font=('courier', 19, 'bold'),command=capture)
button_start.pack(side=tk.TOP,pady=30,padx=20)

button_stop=Button(frame_middle, text='\u12A0\u1241\u121D '
                   ,height=2,width=8, bg='#84D2C5',
                   font=('courier', 19,'bold'),command=btnClickFunction)
button_stop.pack(side=tk.BOTTOM)



#the photo part
label=Label(root,width=628,height=482)

image = Image.open("C:\\Users\\sures\\Downloads\\sign.jpg")
        # Resize the image using resize() method
resize_image = image.resize((628, 482))

img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
label = Label(image=img)
label.image = img
label.pack(side=tk.TOP,pady=5)


frame_bottom=Frame(root,width=100,height=100,bg='light cyan')
frame_bottom.pack(side=tk.TOP)

button_display=Button(frame_bottom, text='test',state=DISABLED,
                      height=2,width=20,fg='light cyan',
                      font=('courier', 19, 'bold'))
button_display.pack(side=tk.TOP,pady=10)

root.mainloop()

