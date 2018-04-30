"""
这是一个演示程序
"""
import qrcode
qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=5
)
qr.add_data("""BEGIN:VCARD
VERSION:3.0
FN:岳润雨
TEL;CELL;VOICE:15001306329
TEL;WORK;VOICE:010-59738891
EMAIL;PREF;INTERNET:yuerunyu@byzoro.com
X-QQ:237003703
URL:http://byzoro.com
ROLE:SDN产品部
TITLE:测试工程师
ADR;WORK;POSTAL:北京市海淀区中关村环保园地锦路5号院3号楼百卓大厦;100095
END:VCARD
""")
qr.make(fit=True)
img = qr.make_image()
img.save(r"E:\pycharm\PycharmProjects\pytest_demo\src\basic\create_qr\qrcode.png")
