"""
function 学习强国题库
from 冬眠的int21h
made by 2021.1.15
"""
import requests
import re
from PIL import Image
import erzhihua
import aircv as ac
from aip import AipOcr


# 图片匹配
def matchImg(imgsrc, imgobj, confidence=0.98):
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, confidence)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result


# 二值化处理
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


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 获取图片地址
def get_image_internet(url):
    # url = 'http://ks51.100xuexi.com/SubItem/NoticeDetail.aspx?id=a95d1661-5146-4449-a325-823a23285325'
    strhtml = requests.get(url)
    pattern = r'https://appfileoss-tw.100xuexi.com/Upload/XuexiAgent/Images/.*?\.jpg'
    ht = re.findall(pattern, strhtml.text)
    return ht, len(ht)


# 保存图片
def image_save(ht, ab=0):
    for i in range(1, len(ht)):
        response = requests.get(ht[i])
        file_name = '.\\image\\' + 'source' + '.jpg'
        file_name1 = '.\\image\\' + str(i + ab) + 'left' + '.jpg'
        file_name2 = '.\\image\\' + str(i + ab) + 'right' + '.jpg'
        with open(file_name, 'wb') as f:
            f.write(response.content)
        f.close()
        img = Image.open(file_name)
        image = black(img, 100)
        image1 = image.crop((0, 0, 535, 1520))
        image2 = image.crop((540, 0, 1075, 1520))
        image1.save(file_name1)
        image2.save(file_name2)


# 题库生成  #调用了百度ai的接口，可以免费注册使用
def get_words(n):
    APP_ID = 'xxxxxxx'
    API_KEY = 'xxxxxxxxxxxxxxxxxxxxx'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxx'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open('学习强国题库.txt', 'w') as f:
        f.close()
    for i in range(1, n + 1):
        file_name1 = '.\\image\\' + str(i) + 'left' + '.jpg'
        file_name2 = '.\\image\\' + str(i) + 'right' + '.jpg'
        try:
            image1 = get_file_content(file_name1)
            image2 = get_file_content(file_name2)
            a1 = client.basicAccurate(image1)
            a2 = client.basicAccurate(image2)
            result1 = a1['words_result']
            result2 = a2['words_result']
            with open('学习强国题库.txt', 'a') as f:
                for i in range(len(result1)):
                    f.write(result1[i]['words'])
                    # if re.findall(r':[ABCD]', result1[i]['words']):
                    #     f.write('\n')
                for i in range(len(result2)):
                    f.write(result2[i]['words'])
                    # if re.findall(r':[ABCD]', result1[i]['words']):
                    #     f.write('\n')
            f.close()
            print(file_name1 + '和' + file_name2 + '已完成')
        except:
            print(file_name1 + '和' + file_name2 + '不存在')


# 题库格式修正
def to_normal():
    string = ''
    with open('学习强国题库.txt', 'r') as f:
        a = f.readline()
        while a != '':
            for i in range(len(a)):
                if a[i] != '\n':
                    if a[i] == 'A' or a[i] == 'B' or a[i] == 'C' or a[i] == 'D' or a[i] == '8':
                        if a[i - 1] == ':':
                            if a[i] != '8':
                                string += a[i]
                                string += '\n'
                            else:
                                string += 'B\n'
                        else:
                            string += a[i]
                    else:
                        string += a[i]
            a = f.readline()
    f.close()
    with open('学习强国题库.txt', 'w') as f:
        with open('学习强国题库上.txt', 'r') as f2:
            s = f2.read()
            f2.close()
        f.write(s)
        f.write(string)
    f.close()


# 综合
def renew():
    # ht, s = get_image_internet(
    #     'http://ks51.100xuexi.com/SubItem/NoticeDetail.aspx?id=a95d1661-5146-4449-a325-823a23285325')
    # image_save(ht)
    s = 0  # 注释部分为题库前半部分，已被注释，s取0

    ht2, s2 = get_image_internet(
        'http://ks51.100xuexi.com/SubItem/NoticeDetail.aspx?id=02cf0dd5-b2f6-414e-85d1-cb5be2ff5d54')
    image_save(ht2)
    # s2 = 0  # 注释部分为题库后半部分，已被注释，s2取0

    get_words(s + s2)
    to_normal()


if __name__ == '__main__':
    renew()
