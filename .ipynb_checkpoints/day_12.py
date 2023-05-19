
import cv2
from time import sleep

fd = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
sd = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

seq = 0
vid = cv2.VideoCapture(0)
captured = False
while not captured:
    flag,img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #to convert gray color
        # x1,y1,w,h = (200,400,200,200)
        faces = fd.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5,minSize =(100,100))
        
        for x1,y1,w,h in faces:
            face = img_gray[y1:y1+h,x1:x1+w].copy()
            smiles =  sd.detectMultiScale(face,1.1,5,minSize=(50,50))
            print(len(smiles))
            if len (smiles)==1:
                seq += 1
                if seq == 5:
                    captured=cv2.imwrite('selfie.png',img)
                    break
                xs,ys,ws,hs = smiles[0]
                cv2.rectangle(img,pt1=(xs+x1,ys+y1),pt2=(xs+ws+x1,ys+hs+y1),color=(0,255,0),thickness=10)
            else:
                seq = 0
            #cv2.rectangle(img,pt1:=(x1,y1),pt2:=[x1+w,y1+h],color:=(235,130,255),thickness:=1)
        cv2.imshow('Preview',img)
        key = cv2.waitKey(1)
        if key == ord('x'):
            break
    else:
        break;
    sleep(0.1)               #to type any key
vid.release()                    #for close video camaera
cv2.destroyAllWindows()          #for close all windows
cv2.waitKey(1)