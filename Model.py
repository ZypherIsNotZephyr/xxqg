"""
function 封装了学习强国各模块调用的二级函数和通用一级函数
from 冬眠的int21h
made by 2021.1.15
"""
from aip import AipOcr
from PIL import Image
import aircv as ac
import time
import random


# 一级函数：进入学习强国
def setup(d):
    d.app_start("cn.xuexi.android")
    # 不开启存储空间权限
    d(text='取消').click_exists(timeout=5)
    # 点击'我的'
    time.sleep(random.random() + 1)
    d(text='我的').click(offset=(random.random(), random.random()))
    time.sleep(random.random() + 0.4)
    # d.drag(random.random(), random.uniform(0.3, 0.4), random.random(), random.uniform(0.5, 0.6))
    # time.sleep(random.random())
    # 点击'学习积分'
    d(text='学习积分').click(offset=(random.random(), random.random()))
    time.sleep(random.random() + 1)
    # d.drag(0.456, 0.821, 0.475, 0.352)
    d.drag(random.random(), random.uniform(0.8, 0.9), random.random(), random.uniform(0.1, 0.3))
    # time.sleep(random.random() + 1)


# 一级函数：判断积分是否已达上限
def check(d):
    image = d.screenshot()
    image.save('hh.png')
    result = matchImg('hh.png', '.\\image2\\tongyong\\check.png')
    if result is not None:
        print("当前模块已完成")
        return 0
    else:
        return 1


# 二级函数：确定位置
def matchImg(imgsrc, imgobj, confidence=0.98):
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, confidence)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result


# 二级函数:读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 二级函数：图片二值化处理
def black(img, threshold=200):
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化
    photo = Img.point(table, '1')
    photo.save('hh2.png')
    return photo


# 二级函数：获取图片文字
def do_image(swc=True, a=81, b=397, c=998, d=2150):
    # 调用api接口
    # 需要请自行注册，获得这三类密钥填入即可
    APP_ID = 'xxxxx'
    API_KEY = 'xxxxxx'
    SECRET_KEY = 'xxxxxx'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = Image.open('hh.png')
    # swc=true:对图片进行裁剪+二值化处理
    if swc is True:
        image = image.crop((a, b, c, d))
        image = black(image, 100)
    image.save('hh2.png')
    image = get_file_content('hh2.png')
    a = client.basicGeneral(image)
    result = a['words_result']
    answer = ''
    for i in range(len(result)):
        answer += result[i]['words']
    return answer


# 获取模块入口地址px
def enter_px():
    pass
