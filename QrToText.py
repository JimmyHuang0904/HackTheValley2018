import cv2
import numpy as np
import qrtools
import time
from firebase import firebase

cap = cv2.VideoCapture(1) # /dev/video1 . If not then change accordingly
qr = qrtools.QR()
# firebase = firebase.FirebaseApplication("https://htv2-3e7e6.firebaseio.com", None)

# assignedHID = "1"
postFlag = False

# try:
#     assignedHIDLocation = firebase.get('/Locations', assignedHID)
#     print assignedHIDLocation
# except:
#     print("OH NO")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    cv2.imwrite("screenshot.png", gray)

    qr.decode("screenshot.png")
    # print qr.data
    if (qr.data != "NULL") & (postFlag == True):
        uuid = qr.data
        print uuid
        
        file = open("uuid.txt","w") 
        file.write(str(uuid))
        file.close()

        postFlag = False
        qr.data = "NULL"
    else:
        postFlag = True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

try:
    cap.release()
    cv2.destroyAllWindows()
except:
    print("Error")