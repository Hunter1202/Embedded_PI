import time 
import Adafruit_Nokia_LCD as LCD
# Khai bao thu vien pillow de tao hinh va ve
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def main():
    # Khai bao cac pin GPIO
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp #khoi tao bien global
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS) #Khoi tao LCD
    disp.begin(contrast=60) # cai dat do sang
    # xoa man hinh
    disp.clear()
    disp.display()
    # tao anh 1 bit color, voi chieu rong, cao bang cua LCĐ
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    #chon doi tuong de ve
    draw = ImageDraw.Draw(image)
    # vẽ 1 hinh chu nhat mau trang
    draw.rectangle((0,0,LCD.LCDWIDTH-1,LCD.LCDHEIGHT-1), outline=0, fill=255)
    # và cac hinh khac
    draw.ellipse((2,2,22,22), outline=0, fill=255)
    draw.rectangle((24,2,44,22), outline=0, fill=255)
    draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
    draw.line((68,22,81,2), fill=0)
    draw.line((68,2,81,22), fill=0)
    #load font chu de chen. (font chu mac dinh)
    font = ImageFont.load_default()
    draw.text((8,30), 'Hello World!', font=font) #chen chu
    #hien thi hinh anh
    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)
try:
    main()
except KeyboardInterrupt: #xu ly su kien Ctrl+CV
    disp.clear() #xoa man hinh