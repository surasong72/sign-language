Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... from tkinter import *
... from PIL import Image, ImageTk
... import cv2
... from keras.models import model_from_json
... import operator
... import numpy as np
... 
... # Loading the model
... json_file = open("model-bw.json", "r")
... model_json = json_file.read()
... json_file.close()
... loaded_model = model_from_json(model_json)
... loaded_model.load_weights("model-bw.h5")
... print("Loaded model from disk")
... 
... categories = {0: 'Aa', 1: 'ae', 2: 'be', 3: 'che', 4: 'chhe', 5: 'de', 6: 'fe',
...               7: 'guh', 8: 'ha', 9: 'hea', 10: 'hha', 11: 'huh', 12: 'je', 13: 'keh',
...               14: 'le', 15: 'me', 16: 'neh', 17: 'gne', 18: 'pe', 19: 'ppe', 20: 'qeh',
...               21: 're', 22: 'se', 23: 'seh', 24: 'she', 25: 'teh', 26: 'tse', 27: 'tse1',
...               28: 'Tte', 29: 'weh', 30: 'ye', 31: 'ze', 32: 'zjeh'}
... 
... # Function to stop the webcam and reset the GUI
... def stop():
...     button_start['state'] = NORMAL
...     button_stop['state'] = DISABLED
...     button_learn['state'] = NORMAL
... 
...     cap.release()
...     label1.pack_forget()
...     label.pack(side=tk.TOP, pady=5)
...     frame_alphabet.pack_forget()
...     label_display.pack(side=tk.TOP)
...     label_ha.pack_forget()

# Function to handle button click events for learning mode
def clicked(text):
    label1.pack_forget()
    label_ha.pack(side=tk.TOP, pady=5)

# Function to start learning mode
def learn():
    button_start['state'] = NORMAL
    button_stop['state'] = NORMAL
    button_learn['state'] = DISABLED

    label.pack_forget()
    label_display.pack_forget()

    frame_alphabet.pack(side=tk.TOP, pady=5)
    label1.pack(side=tk.TOP, pady=5)

# Function to capture frames from the webcam and make predictions
def capture():
    button_start['state'] = DISABLED
    button_stop['state'] = NORMAL
    button_learn['state'] = NORMAL

    label1.pack_forget()

    # Get the latest frame and convert into Image
    cv2img = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    cv2image = cv2.flip(cv2img, 1)
    im_arr = np.asarray(cv2image)
    img_arr_bgr = cv2.cvtColor(im_arr, cv2.COLOR_RGB2BGR)

    # Drawing the ROI
    image_one = cv2.rectangle(img_arr_bgr, (400, 40), (630, 350), color=(255, 0, 0), thickness=1)
    img_rgb = np.asarray(image_one)
    image_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(image_rgb)
    imgtk = ImageTk.PhotoImage(im)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(1, capture)

    # Extracting the ROI
    roi = image_rgb[40:350, 400:630]
    roi = cv2.resize(roi, (64, 64))
    test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)[1]
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 3))
    prediction = {categories[i]: result[0][i] for i in range(len(categories))}
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    label_display.config(text=prediction[0][0])

# Initialize the GUI
root = Tk()
root.title("\u121D\u120D\u12AD\u1275 \u124B\u1295\u124B")
root.configure(bg="light cyan")
root.maxsize(800, 768)
root.geometry("800x768+270+0")

ico = Image.open('sign.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

cap = cv2.VideoCapture(0)

frame_parent = Frame(root, width=300, height=80)
frame_parent.pack(side=tk.TOP)

label_title = Label(frame_parent, bg='#B9F3FC',
                    text='\u12E8\u12A0\u121B\u122D\u129B \u121D\u120D\u12AD\u1275 \u124B\u1295\u124B \u1218\u121B\u122A\u12EB',
                    height=4, width=60, font=('courier', 19, 'bold'))
label_title.pack()

frame_middle = Frame(root, width=200, height=300, bg='light cyan')
frame_middle.pack(side=tk.RIGHT)

button_start = Button(frame_middle, text='\u1300\u121D\u122D',
                      height=2, width=8, bg='#84D2C5',
                      font=('courier', 19, 'bold'), command=capture)
button_start.pack(side=tk.TOP, pady=30, padx=20)

button_stop = Button(frame_middle, text='\u12A0\u1241\u121D',
                     height=2, width=8, bg='#84D2C5',
                     font=('courier', 19, 'bold'), command=stop)
button_stop.pack(side=tk.TOP)

button_learn = Button(frame_middle, text='\u1218\u121B\u122A\u12EB',
                      height=2, width=8, bg='#84D2C5',
                      font=('courier', 19, 'bold'), command=learn)
button_learn.pack(side=tk.BOTTOM, pady=30, padx=20)

image = Image.open("sign.jpg")
resize_image = image.resize((628, 482))
img = ImageTk.PhotoImage(resize_image)

label = Label(root, image=img)
label.pack(side=tk.TOP, pady=5)

frame_bottom = Frame(root, width=100, height=100, bg='light cyan')
frame_bottom.pack(side=tk.TOP)

label_display = Label(frame_bottom, width=10, height=2,
                      text="", font=('courier', 19, 'bold'), bg="white")
label_display.pack(side=tk.TOP, ipady=20)

image1 = Image.open("amharic-alphabet.jpg")
resize_image1 = image1.resize((628, 482))
img1 = ImageTk.PhotoImage(resize_image1)

label1 = Label(root, image=img1)

frame_alphabet = Frame(frame_bottom, bg='black')

# Add alphabet buttons
buttons = [
    ('\u1200', 'ha'), ('\u1208', 'le'), ('\u1210', 'hha'), ('\u1218', 'me'),
    ('\u1220', 'seh'), ('\u1228', 're'), ('\u1230', 'se'), ('\u1238', 'she'),
    ('\u1240', 'qeh'), ('\u1260', 'be'), ('\u1270', 'te'), ('\u1278', 'che'),
    ('\u1280', 'hea'), ('\u1290', 'neh'), ('\u1298', 'nge'), ('\u12a0', 'Aa'),
    ('\u12a8', 'keh'), ('\u12b8', 'huh'), ('\u12c8', 'weh'), ('\u12d0', 'ae'),
    ('\u12d8', 'ze'), ('\u12e8', 'je'), ('\u12f0', 'de'), ('\u12f8', 'ge'),
    ('\u1308', 'teh'), ('\u1310', 'Tte'), ('\u1320', 'che'), ('\u1328', 'tse'),
    ('\u1338', 'tse1'), ('\u1348', 'guh'), ('\u1358', 'pe'), ('\u1380', 'fe')
]

for button_text, label_text in buttons:
    Button(frame_alphabet, text=button_text, font=('courier', 19, 'bold'), width=5, height=1,
           bg='#84D2C5', command=lambda text=label_text: clicked(text)).pack(side=LEFT, padx=2)

image_ha = Image.open("ha.png")
resize_image_ha = image_ha.resize((628, 482))
img_ha = ImageTk.PhotoImage(resize_image_ha)

label_ha = Label(root, image=img_ha)

root.mainloop()
