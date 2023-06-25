import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CURRECT_L, 
        box_size=15,
        border=6,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')

generate_qrcode("http://www.google.com")