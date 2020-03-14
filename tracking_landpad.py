import cv2
import numpy as np
import serial
import time

ser =  serial.Serial('/dev/ttyUSB0',9600)
             

def  mencari_contour (frame):


# define range of  color in HSV
    #malam lab
    lower_hsv1 = np.array([88,31,65])
    upper_hsv1 = np.array([180,255,255])

    lower_hsv2 = np.array([0,98,93])
    upper_hsv2 = np.array([52,255,255])
    
    mask1 = cv2.inRange(frame, lower_hsv1, upper_hsv1)

    mask2 = cv2.inRange(frame, lower_hsv2, upper_hsv2)
    _,contours, hirearchy = cv2.findContours(mask1,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE,offset=(0, 0))
    for cnt in contours:
        cv2.drawContours(mask1,[cnt],-1,(255, 255, 255),-1)
        #cv2.imshow('mask2',mask1)
    
    mask2 = mask2&mask1
    #cv2.dilate(mask2,(5,5))
    #mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, (3,3))
    return mask2

centerx = 80
centery = 60


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc (*'XVID')
out = cv2.VideoWriter ('tracking_landpad0669.avi', fourcc,30.0, (160,120))
    
if cap.isOpened() == False:
    print ('unable open the camera')
else:
    print ('start grabbing video')
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    
    
    while (cap.isOpened() ):
        ret,frame= cap.read()        
        frame = cv2.resize(frame,(160,120))
           
        if ret == False:
            print ('unable grab camera')
            break
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.circle(frame,(centerx,centery),2,(255,255,255),3) # gambar titik tengah
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        threshold = mencari_contour(hsv)
        _,contours, hirearchy = cv2.findContours(threshold,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE,offset=(0, 0))
        offsetx = -1000
        offsety = -1000
        w = -1000
        h = -1000
        for cnt in contours:
            cv2.drawContours(threshold,[cnt],-1,(255, 255, 255),-1)
            areaK = cv2.contourArea(cnt)
            x,y,w,h = cv2.boundingRect(cnt)
            if (areaK > 20):                
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                             
                cent_rectx = (x+(w/2))
                cent_recty = (y+(h/2))
                offsetx = centerx - cent_rectx
                offsety = centery - cent_recty
            else :
                 offsetx = -1000
                 offsety = -1000
                 w = -1000

        offsetx = str(offsetx)
        offsety = str(offsety)
        w1 = str (w)
        #h1 = str(h)
        #print  ("x = " +str(offsetx) + "y =" + str(offsety) + "w = " + str(w1) +
         #       "h = " + str(h1))
        ser.write(',')
        ser.write(offsetx)
        ser.write(',')
        ser.write(offsety)
        ser.write(',')
        ser.write(w1)
        ser.write(',')
        #ser.write(h1)
        #ser.write(',')
        
        #rekam = cv2.flip(framerec,0)
        out.write(frame)
        cv2.imshow('frame',frame)       
        #cv2.imshow('adda' , mask1) 
        #cv2.imshow('th',threshold)

        k = cv2.waitKey(1)
        if (k == 27) :
             break
        


cap.release()
out.release()
cv2.destroyAllWindows()
