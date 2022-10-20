import qr as qr

qr_code = qr.QRCode(
    version=1,
    box_size=5,
    border=2,
)

qr_code.add_data("A little complicated, but not hard!")
qr_code.make(fit=True)

img = qr_code.make_image()
img.save('image.jpg')
