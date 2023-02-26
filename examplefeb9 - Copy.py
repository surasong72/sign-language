import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
from keras.models import model_from_json
import operator
import sys, os
import numpy as np

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

categories = {0: 'Aa', 1: 'ae', 2: 'be', 3: 'che', 4: 'chhe', 5: 'de',6: 'fe',
              7: 'guh',8: 'ha',9: 'hea', 10: 'hha', 11: 'huh', 12: 'je', 13: 'keh',
              14: 'le',15: 'me',16: 'neh',17: 'gne',18: 'pe', 19: 'ppe', 20: 'qeh',
              21: 're', 22: 'se', 23: 'seh',24: 'she',25: 'teh',26: 'tse',27: 'tse1',
              28: 'Tte', 29: 'weh', 30: 'ye', 31: 'ze', 32: 'zjeh'}
#function for the stop button clicking event
def stop():
        button_start['state']=NORMAL
        button_stop['state']=DISABLED
        button_learn['state']=NORMAL
        
        cap.release()
        label1.pack_forget()
        label.pack(side=tk.TOP,pady=5)
        frame_alphabet.pack_forget()
        label_display.pack(side=tk.TOP)
        

#function for the learn button click event
def learn():
        button_start['state']=NORMAL
        button_stop['state']=NORMAL
        button_learn['state']=DISABLED
        
        label.pack_forget()
        label_display.pack_forget()

        frame_alphabet.pack(side=tk.TOP,pady=5)
        label1.pack(side=tk.TOP,pady=5)

        
        

        
root=Tk()
root.title("\u121D\u120D\u12AD\u1275 \u124B\u1295\u124B")
root.configure(bg="light cyan")
root.maxsize(800,768)
root.geometry("800x768+270+0")

ico = Image.open('sign.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
cap=cv2.VideoCapture(0)
def capture():
        button_start['state']=DISABLED
        button_stop['state']=NORMAL
        button_learn['state']=NORMAL
        
        # Get the latest frame and convert into Image
        cv2img= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        cv2image=cv2.flip(cv2img,1)
        im_arr=np.asarray(img)
        img_arr_bgr=cv2.cvtColor(im_arr,cv2.COLOR_RGB2BGR)

        # Drawing the ROI
        # The increment/decrement by 1 is to compensate for the bounding box
        image_one=cv2.rectangle(img_arr_bgr, (400,40),(630, 350),color=(255,0,0) ,thickness=1)
        img_rgb=np.asarray(image_one)
        image_rgb=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2RGB)
        im=Image.fromarray(image_rgb)
        imgtk = ImageTk.PhotoImage(im)
        label.imgtk= imgtk
        label.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        label.after(1, capture)


        # Extracting the ROI
        roi = image_rgb[40:350, 400:630]
        # Coordinates of the ROI
        # Resizing the ROI so it can be fed to the model for prediction
        roi = cv2.resize(roi, (64, 64))
        test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        #test_image=roi
        # Batch of 1
        result = loaded_model.predict(roi.reshape(1,64,64,3))
        prediction = {'\u12d0': result[0][0], 
                  '\u12a0': result[0][1], 
                  '\u1260': result[0][2],
                  '\u1278': result[0][3],
                  '\u1328': result[0][4],
                  '\u12f0': result[0][5],
                  '\u1348': result[0][6],
                  '\u1290': result[0][7],
                  '\u1200': result[0][8],
                  '\u1280': result[0][9],
                  '\u1210': result[0][10], 
                  '\u12b8': result[0][11],
                  '\u1300': result[0][12],
                  '\u12a8': result[0][13],
                  '\u1208': result[0][14],
                  '\u1218': result[0][15],
                  '\u1290': result[0][16],
                  '\u1298': result[0][17], 
                  '\u1350': result[0][18],
                  '\u1330': result[0][19],
                  '\u1240': result[0][20],
                  '\u1228': result[0][21],
                  '\u1230': result[0][22],
                  '\u1220': result[0][23],
                  '\u1238': result[0][24], 
                  '\u1270': result[0][25],
                  '\u1340': result[0][26],
                  '\u1338': result[0][27],
                  '\u1320': result[0][28],
                  '\u12c8': result[0][29],
                  '\u12e8': result[0][30],
                  '\u12d8': result[0][31], 
                  '\u1300': result[0][32]}

        # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        label_display.config(text=prediction[0][0])

        
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
                   font=('courier', 19,'bold'),command=stop)
button_stop.pack(side=tk.TOP)

button_learn=Button(frame_middle, text='\u1218\u121b\u122a\u12eb'
                   ,height=2,width=8, bg='#84D2C5',
                   font=('courier', 19,'bold'),command=learn)
button_learn.pack(side=tk.BOTTOM,pady=30,padx=20)

#the photo diplay part
image = Image.open("sign.jpg")
        # Resize the image using resize() method
resize_image = image.resize((628, 482))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label = Label(root,image=img)
label.pack(side=tk.TOP,pady=5)

#this is the bottom frame for the displaying of the result
frame_bottom=Frame(root,width=100,height=100,bg='light cyan')
frame_bottom.pack(side=tk.TOP)

label_display=Label(frame_bottom,width=10,height=2,
                    text="",
                    font=('courier', 19, 'bold'),bg="white")
label_display.pack(side=tk.TOP,ipady=20)


#this is the label to display the learn image
image1 = Image.open("amharic-alphabet.jpg")
# Resize the image using resize() method
resize_image1 = image1.resize((628, 482))
img1 = ImageTk.PhotoImage(resize_image1)

# create label and add resize image
label1 = Label(root,image=img1)
        
frame_alphabet=Frame(frame_bottom,width=100,height=100,bg='light cyan')

button_ha=Button(frame_alphabet,text='\u1200', bg='#DC8449',font=('courier', 15,'bold'))
button_ha.pack(side=LEFT,padx=5)

button_le=Button(frame_alphabet,text='\u1208', bg='#DC8449',font=('courier', 15,'bold'))
button_le.pack(side=LEFT,padx=5)

button_hha=Button(frame_alphabet,text='\u1210', bg='#DC8449',font=('courier', 15,'bold'))
button_hha.pack(side=LEFT,padx=5)

button_me=Button(frame_alphabet,text='\u1218', bg='#DC8449',font=('courier', 15,'bold'))
button_me.pack(side=LEFT,padx=5)

button_seh=Button(frame_alphabet,text='\u1220', bg='#DC8449',font=('courier', 15,'bold'))
button_seh.pack(side=LEFT,padx=5)

button_re=Button(frame_alphabet,text='\u1228', bg='#DC8449',font=('courier', 15,'bold'))
button_re.pack(side=LEFT,padx=5)

button_se=Button(frame_alphabet,text='\u1230', bg='#DC8449',font=('courier', 15,'bold'))
button_se.pack(side=LEFT,padx=5)

button_she=Button(frame_alphabet,text='\u1238', bg='#DC8449',font=('courier', 15,'bold'))
button_she.pack(side=LEFT,padx=5)

button_qeh=Button(frame_alphabet,text='\u1240', bg='#DC8449',font=('courier', 15,'bold'))
button_qeh.pack(side=LEFT,padx=5)

button_be=Button(frame_alphabet,text='\u1260', bg='#DC8449',font=('courier', 15,'bold'))
button_be.pack(side=LEFT,padx=5)

button_te=Button(frame_alphabet,text='\u1270', bg='#DC8449',font=('courier', 15,'bold'))
button_te.pack(side=LEFT,padx=5)

button_che=Button(frame_alphabet,text='\u1278', bg='#DC8449',font=('courier', 15,'bold'))
button_che.pack(side=LEFT,padx=5)

button_hea=Button(frame_alphabet,text='\u1280', bg='#DC8449',font=('courier', 15,'bold'))
button_hea.pack(side=LEFT,padx=5)

button_neh=Button(frame_alphabet,text='\u1290', bg='#DC8449',font=('courier', 15,'bold'))
button_neh.pack(side=LEFT,padx=5)

button_nge=Button(frame_alphabet,text='\u1298', bg='#DC8449',font=('courier', 15,'bold'))
button_nge.pack(side=LEFT,padx=5)

button_Aa=Button(frame_alphabet,text='\u12a0', bg='#DC8449',font=('courier', 15,'bold'))
button_Aa.pack(side=LEFT,padx=5)

button_keh=Button(frame_alphabet,text='\u12a8', bg='#DC8449',font=('courier', 15,'bold'))
button_keh.pack(side=LEFT,padx=5)

button_huh=Button(frame_alphabet,text='\u12b8', bg='#DC8449',font=('courier', 15,'bold'))
button_huh.pack(side=LEFT,padx=5)

button_weh=Button(frame_alphabet,text='\u12c8', bg='#DC8449',font=('courier', 15,'bold'))
button_weh.pack(side=LEFT,padx=5)

button_ae=Button(frame_alphabet,text='\u12d0', bg='#DC8449',font=('courier', 15,'bold'))
button_ae.pack(side=LEFT,padx=5)

button_ze=Button(frame_alphabet,text='\u12d8', bg='#DC8449',font=('courier', 15,'bold'))
button_ze.pack(side=LEFT,padx=5)

button_zjeh=Button(frame_alphabet,text='\u12e0', bg='#DC8449',font=('courier', 15,'bold'))
button_zjeh.pack(side=LEFT,padx=5)

button_ye=Button(frame_alphabet,text='\u12e8', bg='#DC8449',font=('courier', 15,'bold'))
button_ye.pack(side=LEFT,padx=5)

button_de=Button(frame_alphabet,text='\u12f0', bg='#DC8449',font=('courier', 15,'bold'))
button_de.pack(side=LEFT,padx=5)

button_je=Button(frame_alphabet,text='\u12f8', bg='#DC8449',font=('courier', 15,'bold'))
button_je.pack(side=LEFT,padx=5)

button_guh=Button(frame_alphabet,text='\u1308', bg='#DC8449',font=('courier', 15,'bold'))
button_guh.pack(side=LEFT,padx=5)

button_Tte=Button(frame_alphabet,text='\u1320', bg='#DC8449',font=('courier', 15,'bold'))
button_Tte.pack(side=LEFT,padx=5)

button_chhe=Button(frame_alphabet,text='\u1328', bg='#DC8449',font=('courier', 15,'bold'))
button_chhe.pack(side=LEFT,padx=5)

button_ppeh=Button(frame_alphabet,text='\u1330', bg='#DC8449',font=('courier', 15,'bold'))
button_ppeh.pack(side=LEFT,padx=5)

button_tse1=Button(frame_alphabet,text='\u1338', bg='#DC8449',font=('courier', 15,'bold'))
button_tse1.pack(side=LEFT,padx=5)

button_tse=Button(frame_alphabet,text='\u1340', bg='#DC8449',font=('courier', 15,'bold'))
button_tse.pack(side=LEFT,padx=5)

button_fe=Button(frame_alphabet,text='\u1348', bg='#DC8449',font=('courier', 15,'bold'))
button_fe.pack(side=LEFT,padx=5)

button_peh=Button(frame_alphabet,text='\u1350', bg='#DC8449',font=('courier', 15,'bold'))
button_peh.pack(side=LEFT,padx=5)


root.mainloop()

