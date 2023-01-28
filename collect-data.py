import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/che")
    os.makedirs("data/train/gne")
    os.makedirs("data/train/ha")
    os.makedirs("data/train/hee")
    os.makedirs("data/train/ke")
    os.makedirs("data/train/le")
    os.makedirs("data/train/me")
    os.makedirs("data/train/ne")
    os.makedirs("data/train/qe")
    os.makedirs("data/test/che")
    os.makedirs("data/test/gne")
    os.makedirs("data/test/ha")
    os.makedirs("data/test/hee")
    os.makedirs("data/test/ke")
    os.makedirs("data/test/le")
    os.makedirs("data/test/me")
    os.makedirs("data/test/ne")
    os.makedirs("data/test/qe")
    

# Train or test 
mode = 'train'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'che': len(os.listdir(directory+"/che")),
             'gne': (len(os.listdir(directory+"/gne"))+286),
             'ha': (len(os.listdir(directory+"/ha"))+503),
             'hee': (len(os.listdir(directory+"/hee"))+1208),
             'ke': (len(os.listdir(directory+"/ke"))+848),
             'le': (len(os.listdir(directory+"/le"))+409),
             'me': (len(os.listdir(directory+"/me"))+1412),
             'ne': (len(os.listdir(directory+"/ne"))+667),
             'qe': (len(os.listdir(directory+"/qe"))+1137)}
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "che : "+str(count['che']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "gne : "+str(count['gne']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ha : "+str(count['ha']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "hee : "+str(count['hee']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ke : "+str(count['ke']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "le : "+str(count['le']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ne : "+str(count['ne']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "qe : "+str(count['qe']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)

        
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (100,100)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    #roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
    #_, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    roi = cv2.resize(roi, (500,420))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'che/'+str(count['che'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'gne/'+'gne'+str(count['gne'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'ha/'+'he'+str(count['ha'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'hee/'+'hhe'+str(count['hee'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'ke/'+'ke'+str(count['ke'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'le/'+'Le'+str(count['le'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'me/'+'Me'+str(count['me'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'ne/'+'ne'+str(count['ne'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'qe/'+'qe'+str(count['qe'])+'.jpg', roi)
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
