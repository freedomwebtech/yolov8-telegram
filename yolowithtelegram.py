
import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
import datetime
from time import sleep
import telepot

model=YOLO('best.pt')
image_sent=False
bot_token = '5955954381:AAGY9ttUXlrclgDMt8j8QWAUvaERDEIM6Vo'
bot = telepot.Bot(bot_token)

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture(0)


my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
area=[(605,292),(531,322),(743,354),(766,307)]
while True:

    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
   

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    
    
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),2)
        cvzone.putTextRect(frame,f'{c}',(x1,y1),1,2)   
        if 'no-helmet' in c and not image_sent:
           current_datetime = datetime.datetime.now()
           image_filename = f'no-helmet{current_datetime.strftime("%d-%m-%Y_%H-%M-%S")}.png'
           cv2.imwrite(image_filename, frame)
#        print(f"Captured and sent image: {image_filename}")
           with open(image_filename, 'rb') as image_file:
                bot.sendPhoto(chat_id='6526920307', photo=image_file, caption='Hello, message with an image!')
              
    
    
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
