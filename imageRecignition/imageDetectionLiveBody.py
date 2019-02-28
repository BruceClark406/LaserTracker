import cv2
import numpy as np

upperBodyCascade = cv2.CascadeClassifier('C:/Users/bruce/Downloads/opencv/sources/data/haarcascades/haarcascade_upperbody.xml')

cap = cv2.VideoCapture(1)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = upperBodyCascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
