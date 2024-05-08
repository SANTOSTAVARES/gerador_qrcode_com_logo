# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
Logo_link = 'foto.jpg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 300

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
# logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
logo = logo.resize((basewidth, hsize))
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://google.com'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Black'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('qrcode_com_logo.png')

