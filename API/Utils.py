import qrcode
from PIL import Image

class QRcode:
    def __init__(self):
        self.version = 1
        self.error_correction = qrcode.constants.ERROR_CORRECT_H
        self.box_size = 10
        self.border = 2
        self.fit = True
        self.logoBaseSize = 100

    def generate(self, data, logo=None) -> Image.Image:
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(data)
        qr.make(fit=self.fit)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        if logo is None:
            return qr_img

        _logo = Image.open(logo)
        basewidth = self.logoBaseSize
        wpercent = (basewidth / float(_logo.size[0]))
        hsize = int((float(_logo.size[1]) * float(wpercent)))
        _logo = _logo.resize((basewidth, hsize), Image.LANCZOS)
        pos = ((qr_img.size[0] - _logo.size[0]) // 2, (qr_img.size[1] - _logo.size[1]) // 2)
        qr_img.paste(_logo, pos)
        return qr_img



if __name__ == "__main__":
    #IMG = QRcode().generate("https://www.facebook.com/ref.robotics", r"E:\REF\REF_API2\static\REF.jpg")
    QR = QRcode()
    QR.logoBaseSize = 70
    IMG = QR.generate("asdadgadf", r"E:\REF\REF_API2\static\REF.jpg")
    IMG.show()
