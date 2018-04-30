"""
这个程序也是生成二维码，但是不同的是二维码中有图片
作者：岳润雨
日期：2017-11-3
"""
from PIL import Image
import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1)

qr.add_data("岳润雨")
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon = Image.open(r"E:\pycharm\image_test.png") #用于填充的图片

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
img.paste(icon, (w, h), icon)

img.save(r"E:\pycharm\PycharmProjects\pytest_demo\src\basic\create_qr\filled_qrcode.png")