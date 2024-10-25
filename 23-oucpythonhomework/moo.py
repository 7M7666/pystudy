import qrcode
from PIL import Image

# 创建一个带有中心图标的QR码
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
data=Image.open("666.jpg")
qr.add_data(data)
qr.make()

# 生成QR码图像
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# 加载logo图像并插入到QR码中心
logo = Image.open('666.jpg')
logo.thumbnail((100, 100))
logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, logo_pos)

# 保存生成的QR码
img.save('22.png')