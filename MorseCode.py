#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2

#Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

first_read = True
#Starting the video capture

cap = cv2.VideoCapture(0)
ret,img = cap.read()
lisst =[]
lisst2 = []
lisst3 = []
msg = []
while(ret):
    ret,img = cap.read()
    #Coverting the recorded image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detecting the face for region of image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.1, 5,minSize=(200,200))
    if(len(faces)>0):
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            #roi_face is face which is input to eye classifier
            roi_face = gray[y:y+h,x:x+w]
            roi_face_clr = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_face,1.3,6)#,minSize=(50,50))
           # lisst = [0]
            #Examining the length of eyes object for eyes
            if(len(eyes)>=2):
                #Check if program is running for detection 
                if(first_read):
                    cv2.putText(img, "Eye detected press s to begin", (70,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)
                else:
                    cv2.putText(img, "Eyes open!", (70,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)
                    lisst2.append(1)
                    if len(lisst) <7 and len(lisst)!=0:
                  #      print("short blink")
                        lisst.clear()
                        lisst3.append("dot")
                        lisst2.clear()
                    elif len(lisst) >7:
                 #       print("long blink")
                        lisst.clear()
                        lisst2.clear()
                        lisst3.append("dash")
                    if len(lisst2) >20:

                   #     print("change letter")
                        cv2.putText(img, "Next letter!", (70,470), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)
                   #     print(lisst3)
                        if lisst3 == ["dot", "dash"]:
                            msg.append("A")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dot", "dot", "dot"]:
                            msg.append("B")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dot", "dash", "dot"]:
                            msg.append("C")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dot", "dot"]:
                            msg.append("D")
                            lisst3.clear()
                        elif lisst3 == ["dot"]:
                            msg.append("E")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dot","dash","dot"]:
                            msg.append("F")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dash","dot"]:
                            msg.append("G")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dot", "dot", "dot"]:
                            msg.append("H")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dot"]:
                            msg.append("I")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dash", "dash", "dash"]:
                            msg.append("J")
                            lisst3.clear()
                        elif lisst3 == ["dash","dot","dash"]:
                            msg.append("K")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dash","dot","dot"]:
                            msg.append("L")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dash"]:
                            msg.append("M")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dot"]:
                            msg.append("N")
                            lisst3.clear()
                        elif lisst3 == ["dash", "dash","dash"]:
                            msg.append("O")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dash","dash","dot"]:
                            msg.append("P")
                            lisst3.clear()
                            
                        elif lisst3 == ["dash","dash","dot", "dash"]:
                            msg.append("Q")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dash"]:
                            msg.append("R")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dot","dot"]:
                            msg.append("S")
                            lisst3.clear()
                        elif lisst3 == ["dash"]:
                            msg.append("T")
                            lisst3.clear()
                        elif lisst3 == ["dot","dot", "dash"]:
                            msg.append("U")
                            lisst3.clear()
                        elif lisst3 == ["dot","dot","dot","dash"]:
                            msg.append("V")
                            lisst3.clear()
                        elif lisst3 == ["dot", "dash", "dash"]:
                            msg.append("W")
                            lisst3.clear()
                        elif lisst3 == ["dash","dot","dot", "dash"]:
                            msg.append("X")
                            lisst3.clear()
                        elif lisst3 == ["dash","dot", "dash","dash"]:
                            msg.append("Y")
                            lisst3.clear()
                        elif lisst3 == ["dash","dash","dot", "dot"]:
                            msg.append("Z")
                            lisst3.clear()
                        elif lisst3 == ["dot","dot","dot","dot","dot","dot","dot"]:
                            msg.append(" ")
                       # lisst3.clear()
                        lisst2.clear()
            else:
                if(first_read):
                    #To ensure if the eyes are present before starting
                    cv2.putText(img, "No eyes detected", (70,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)
                else:
                    #This will print on console and restart the algorithm
                 #   print("Blink detected--------------")
                    lisst.append(1)
                   # cv2.waitKey(3000)
                    first_read=True
          #  print(lisst[-6:-1])
    #        if lisst2[-22:-1] == con2:
        #        print("eyes are indeed open")
        #        lisst2.clear()
        #    if lisst[-45:-1] == con:
       #         print("that's a code")
       #         lisst.clear()
                        
    else:
        cv2.putText(img,"No face detected",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)
        #lisst3.append(1)
    #Controlling the algorithm with keys
    cv2.imshow('img',img)
    a = cv2.waitKey(1)
    if(a==ord('q')):
        break
    elif(first_read):
        #This will start the detection
        first_read = False

cap.release()
cv2.destroyAllWindows()
for i in msg:
    print(i,end = '')


# In[ ]:




