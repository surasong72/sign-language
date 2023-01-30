import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def btnClickFunction():
	root.destroy()
	#cap.release()

root=Tk()
root.title("\u121D\u120D\u12AD\u1275 \u124B\u1295\u124B")
root.configure(bg="light cyan")
root.maxsize(800,700)
root.geometry("700x600+270+30")

frame_parent=Frame(root,width=300,height=100)
frame_parent.pack(side=tk.TOP)

label_title=Label(frame_parent,bg='#B9F3FC',
                  text='\u12E8\u12A0\u121B\u122D\u129B \u121D\u120D\u12AD\u1275 \u124B\u1295\u124B \u1218\u121B\u122A\u12EB',
                  height=4,width=60,font=('courier', 19, 'bold'))
label_title.pack()

frame_middle=Frame(root,width=200,height=300,bg='light cyan')
frame_middle.pack(side=tk.RIGHT)

button_start=Button(frame_middle, text='\u1300\u121D\u122D',
                    height=2,width=8,bg='#84D2C5',
                    font=('courier', 19, 'bold'))
button_start.pack(side=tk.TOP,pady=30,padx=20)

button_stop=Button(frame_middle, text='\u12A0\u1241\u121D '
                   ,height=2,width=8, bg='#84D2C5',
                   font=('courier', 19,'bold'),command=btnClickFunction)
button_stop.pack(side=tk.BOTTOM)



#the photo part
label=Label(root,width=470,height=300)

image = Image.open("C:\\Users\\sures\\Downloads\\sign.jpg")
        # Resize the image using resize() method
resize_image = image.resize((470, 300))

img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
label = Label(image=img)
label.image = img
label.pack(side=tk.LEFT)

frame_bottom=Frame(root,width=100,height=100,bg='light cyan')
frame_bottom.pack(side=BOTTOM)

button_display=Button(frame_bottom, text='test',state=DISABLED,
                      height=2,width=20,fg='light cyan',
                      font=('courier', 19, 'bold'))
button_display.pack(side=tk.TOP,pady=30)

root.mainloop()

