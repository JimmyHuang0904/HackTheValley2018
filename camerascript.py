import cv2
import numpy as np
import qrtools
import time
from firebase import firebase

cap = cv2.VideoCapture(1) # /dev/video1 . If not then change accordingly
qr = qrtools.QR()
firebase = firebase.FirebaseApplication("https://htv2-3e7e6.firebaseio.com", None)

# assignedHID = "1"
postFlag = False
previous = "NULL"

count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    cv2.imwrite("screenshot.png", gray)

    qr.decode("screenshot.png")
    count = count + 1
    if count >= 150:
        count = 150

    if (qr.data != "NULL") & (count >= 30) & (qr.data != previous):
        count = 0

        uuid = qr.data
        previous = uuid
        # print uuid
        try:
            result = firebase.get('/Users/' + uuid, 'assignedHID')
            # print result
            result = firebase.patch('/Scanner/', {'assignedUID': uuid})
            # result = firebase.patch('/Scanner/', {'scanned': True})

        except:
            print "Error"

        qr.data = "NULL"

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
