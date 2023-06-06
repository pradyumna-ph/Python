import qrcode

data = "Hello, World!"

qr = qrcode.QRCode(version=1, box_size=12, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.png")
