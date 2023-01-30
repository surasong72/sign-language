import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
from keras.models import model_from_json
import operator
import sys, os

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

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
    while True:
        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        # Simulating mirror image
        frame = cv2.flip(cv2image, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])# Drawing the ROI# The increment/decrement by 1 is to compensate for the bounding box
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        # Extracting the ROI
        roi = frame[y1:y2, x1:x2]
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(img)
        label.imgtk= imgtk
        label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        label.after(20, capture)

        # Got this from collect-data.py
        # Coordinates of the ROI
        # Resizing the ROI so it can be fed to the model for prediction
        roi = cv2.resize(roi, (64, 64))
        #roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
        test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        test_image=roi
        # Batch of 1
        result = loaded_model.predict(test_image.reshape(1,64,64,3))
        prediction = {'che': result[0][0], 
                  'gne': result[0][1], 
                  'ha': result[0][2],
                  'hee': result[0][3],
                  'ke': result[0][4],
                  'le': result[0][5],
                  'me': result[0][6],
                  'ne': result[0][7],
                  'qe': result[0][8]}
        # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    
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

