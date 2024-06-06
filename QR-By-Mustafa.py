import qrcode
#in cmd :pip install qrcode
msg = "https://www.youtube.com/watch?v=NLARSgB4pqw"
QR = qrcode.make(msg)
QR.save("QR-By-Mustafa.jpg")