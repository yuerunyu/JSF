"""
这是一个课后作业题：
为员工生成二维码名片
1、读取文本文件，里边有3条员工信息；
作者：岳润雨
日期：2017.11.2
"""
import qrcode
def qrcode_gen():
    f=open(r'E:\pycharm\PycharmProjects\pytest_demo\src\basic\create_qr\card_test.txt','r')
    qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=1)
    #这里创建了一个qrcode对象
    """version：值为1~40的整数，控制二维码的大小（最小值是1，是个21×21的矩阵）
    error_correction：控制二维码的错误纠正功能。可取值下列4个常量。 
    ERROR_CORRECT_L：大约7%或更少的错误能被纠正。 
    ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。 
    ERROR_CORRECT_Q ： 25 %以下的错误会被纠正 
    ROR_CORRECT_H：大约30%或更少的错误能被纠正
    box_size：控制二维码中每个小格子包含的像素数。
    border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4）"""
    i=9
    for each_line in f :
        # print(each_line,end="")
        # print(each_line.split(','))
        l1=each_line.split(',')
        # print(type(l1))
        qr.add_data("""BEGIN:VCARD
                        VERSION:3.0
                        FN:%s
                        TEL;CELL;VOICE:%s
                        END:VCARD""" % (l1[0],l1[1]))
        qr.make(fit=True)
        img = qr.make_image()#生成二维码图片
        i+=1
        qr.clear()
        img.save("E:\\pycharm\\PycharmProjects\\pytest_demo\\src\\basic\\create_qr\\qrcode_张%d.png" %i)
        #将图片保存下来
    f.close()
if __name__=="__main__":
    qrcode_gen()