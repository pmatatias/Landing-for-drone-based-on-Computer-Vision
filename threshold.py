import cv2
import numpy as np




def nothing (x):
    print("Trackbar value: " + str(x))
    pass



cv2.namedWindow ('th1',cv2.WINDOW_NORMAL)
cv2.namedWindow ('th2',cv2.WINDOW_NORMAL)


# create trackbars for Upper HSV
cv2.createTrackbar('UpperH','th1',0,255,nothing)
cv2.createTrackbar('UpperS','th1',0,255,nothing)
cv2.createTrackbar('UpperV','th1',0,255,nothing)
# create trackbars for Lower HSV
cv2.createTrackbar('LowerH','th1',0,255,nothing)
cv2.createTrackbar('LowerS','th1',0,255,nothing)
cv2.createTrackbar('LowerV','th1',0,255,nothing)

# create trackbars for Upper HSV2
cv2.createTrackbar('UpperH','th2',0,255,nothing)
cv2.createTrackbar('UpperS','th2',0,255,nothing)
cv2.createTrackbar('UpperV','th2',0,255,nothing)
# create trackbars for Lower HSV2
cv2.createTrackbar('LowerH','th2',0,255,nothing)
cv2.createTrackbar('LowerS','th2',0,255,nothing)
cv2.createTrackbar('LowerV','th2',0,255,nothing)
font = cv2.FONT_HERSHEY_SIMPLEX

  
cap = cv2.VideoCapture ('olah.mp4')
#frame = cv2.imread  ('landasan.jpg')
if cap.isOpened() == False:
    print ('unable open the camera')
while (1):
        ret,frame= cap.read()
        frame = cv2.resize(frame,(180,180))
        
        if ret == False:
           print ('unable grab camera')
           break # get current positions of Upper HSV trackbars
        uh2 = cv2.getTrackbarPos('UpperH','th2')
        us2 = cv2.getTrackbarPos('UpperS','th2')
        uv2 = cv2.getTrackbarPos('UpperV','th2')
        
        # get current positions of Lower HScv2 trackbars
        lh2 = cv2.getTrackbarPos('LowerH','th2')
        ls2 = cv2.getTrackbarPos('LowerS','th2')
        lv2 = cv2.getTrackbarPos('LowerV','th2')
        upper_hsv2 = np.array([uh2,us2,uv2])
        lower_hsv2 = np.array([lh2,ls2,lv2])

        # get current positions of Upper HSV trackbars
        uh1 = cv2.getTrackbarPos('UpperH','th1')
        us1 = cv2.getTrackbarPos('UpperS','th1')
        uv1 = cv2.getTrackbarPos('UpperV','th1')
        
        # get current positions of Lower HScv2 trackbars
        lh1 = cv2.getTrackbarPos('LowerH','th1')
        ls1 = cv2.getTrackbarPos('LowerS','th1')
        lv1 = cv2.getTrackbarPos('LowerV','th1')
        upper_hsv1 = np.array([uh1,us1,uv1])
        lower_hsv1 = np.array([lh1,ls1,lv1])    


        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, lower_hsv1, upper_hsv1)
        mask2 = cv2.inRange(hsv, lower_hsv2, upper_hsv2)
        mask = np.zeros(mask1.shape,np.uint8)
        contours, hirearchy = cv2.findContours(mask1,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE,offset=(0, 0))
        #cv.FindContours(mask, contours, mode=CV_RETR_LIST, method=CV_CHAIN_APPROX_SIMPLE, offset=(0, 0))
        #cnt = contours [0]
        for cnt in contours:
            #cv2.drawContours(mask1,[cnt],-1,(255, 255, 255),-1)
            #cv2.imshow ('output', mask1)
            o = 1
        #mask2 = mask2&mask1
            

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
                
       

        cv2.imshow ('th1',mask1)
        cv2.imshow ('th2',mask2)
        #cv2.imshow ('mask1',mask1)
        #cv2.imshow ('mask2',mask2)        
        #cv2.imshow( 'hsv',hsv)
        #cv2.imshow ('th',frame)
    

cv2.destroyAllWindows()
