"""
function 学习强国[挑战答题]模块
from 冬眠的int21h
made by 2021.1.15
"""
import difflib
import random
import time
import Model


# 进入挑战答题
def go_tzdt(d):
    time.sleep(random.random())
    # 点击'我要答题'
    d.xpath('//android.widget.ListView/android.view.View[8]/android.view.View[4]').click()
    time.sleep(random.uniform(4, 6))
    # # 点击'我要答题'
    # d.click(random.randint(800, 960), random.randint(900, 1050))
    # time.sleep(random.uniform(1, 2))
    # # 点击'挑战答题'
    # d.click(random.randint(560, 1000), random.randint(1480, 1735))
    # time.sleep(random.uniform(2, 3))


# 搜索题库，寻找最优匹配项
def get_answer(answer):
    max_ = -1  # 匹配的最大相似度
    number = -1  # 最优匹配的标号
    with open('text2.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            str2 = lines[i]
            seq = difflib.SequenceMatcher(None, answer, str2)
            ratio = seq.ratio()
            if ratio > max_:
                max_ = ratio
                number = i
        print('当前题目搜索完成，,已获取最优匹配结果，匹配相似度为：' + str(max_))
        print('匹配到的题目为：' + lines[number][:-1])
        print('答案是：' + lines[number][-2] + '\n')
    f.close()
    # 返回答案
    return lines[number][-2]


# 获取错误答案：用于退出答题循环
def get_wrong(answer):
    wrong = answer
    while wrong == answer:
        wrong = random.choice('AB')
    return wrong


# 解析坐标
def get_xp(answer, result):
    if answer == 'C':
        x = int(result[0]) - random.randint(100, 400)
        y = int(result[1]) + random.randint(113, 133)
    elif answer == 'B':
        x = int(result[0]) - random.randint(100, 400)
        y = int(result[1]) + random.randint(80, 100)
    elif answer == 'A':
        x = int(result[0]) - random.randint(100, 400)
        y = int(result[1]) + random.randint(-10, 10)
    elif answer == 'D':
        x = int(result[0]) - random.randint(100, 400)
        y = int(result[1]) + random.randint(255, 270)
    return x, y


# 挑战答题
def to_tzdt(d):
    # 进入挑战答题
    go_tzdt(d)
    i = 0  # 答题数量
    wrong = ''  # 错误答案
    while i < 8:
        image = d.screenshot()
        image.save('hh.png')
        question = Model.do_image()  # 获取题目
        answer = get_answer(question)  # 寻找最优答案(A B C D)中的一个
        if i == 7:
            answer = get_wrong(answer)
            print("已到答题序列上限，获得错误答案：" + answer)
        position = Model.matchImg('hh.png', '.\\image2\\tiaozhandati\\' + str(answer) + '.png')  # 匹配答案位置
        if position is not None:
            result = position['result']  # 获得位置信息(中心位置)
        else:
            result = [555, 1147]
        x, y = get_xp(answer, result)  # 将位置信息用像素表示(实际位置):已随机处理
        d.click(x, y)
        time.sleep(random.uniform(2, 4))
        i += 1
    # 退出
    # d(text="结束本局").click()  # 更换随机点击模式
    # d.click(random.randint(110, 520), random.randint(1460, 1570))
    d(text='结束本局').click(offset=(random.random(), random.random()))
    time.sleep(random.uniform(0.5, 1.5))
    # 返回'学习积分'
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(0.5, 1))


# 合并
def tzdt(d):
    print("正在进入挑战答题模块\n\n")
    while Model.check(d):
        to_tzdt(d)
    time.sleep(random.uniform(0.5, 1.5))
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(1.5, 2))
