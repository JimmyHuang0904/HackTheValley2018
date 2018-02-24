# from qrtools import QR

# import os

# my_QR = QR(data = u"Example")
# my_QR.encode()
 
# # command to move the QR code to the desktop
# os.system("sudo mv " + my_QR.filename + " ~/GitHub/HackTheValley2018")


# my_QR = QR(filename = "/home/jimmy/GitHub/HackTheValley2018/asdf.png")
 
# # decodes the QR code and returns True if successful
# my_QR.decode()
 
# # prints the data
# print my_QR.data

import qrtools
qr = qrtools.QR()
qr.decode("asdf.png")
print qr.data

#sudo apt-get install scrot
