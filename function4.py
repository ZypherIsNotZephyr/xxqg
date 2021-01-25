"""
function 学习强国[争上游答题][双人对战]模块
from 冬眠的int21h
made by 2021.1.23
"""
import difflib
import random
import time
import Model


# 进入争上游答题
def go_zsydt(d, first=True):
    time.sleep(random.random())
    if first is True:
        d.drag(random.random(), random.uniform(0.3, 0.4), random.random(), random.uniform(0.5, 0.6))
        time.sleep(random.random())
        # d.xpath('//android.widget.ListView/android.view.View[9]/android.view.View[4]').click()
        # 改为随机化点击
        # 点击'我要答题'
        d.click(random.randint(800, 960), random.randint(900, 1050))
        time.sleep(random.uniform(1, 2))
    # 点击'争上游答题'
    d.click(random.randint(50, 520), random.randint(1200, 1600))
    time.sleep(random.uniform(0.5, 1.25))
    # 点击'开始比赛'
    d.click(random.randint(300, 700), random.randint(1805, 1960))
    print("waiting")
    time.sleep(random.uniform(11.6, 12))
    print("waiting over")


# 进入双人对战
def go_srdz(d):
    time.sleep(random.random())
    # 点击'双人对战'
    d.click(random.randint(555, 1000), random.randint(1120, 1400))
    time.sleep(random.uniform(0.5, 1.25))
    # 点击'随机匹配'
    d.click(random.randint(739, 834), random.randint(983, 1118))
    print("waiting")
    time.sleep(random.uniform(12.5, 13))
    print("waiting over")


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


# 解析坐标
def get_xp(result):
    x = int(result[0]) + random.randint(0, 500)
    y = int(result[1]) + random.randint(-25, 25)
    return x, y


# 争上游答题
def to_zsydt(d, first=True):
    # 进入争上游答题
    go_zsydt(d, first)
    i = 0
    while 1:
        image = d.screenshot()
        image.save('hh.png')
        question = Model.do_image(a=70, b=670, c=1000, d=2175)  # 获取题目
        answer = get_answer(question)  # 寻找最优答案(A B C D)中的一个
        position = Model.matchImg('hh.png', '.\\image2\\zhengshangyou\\' + str(answer) + '.png')  # 匹配答案位置
        if position is not None:
            result = position['result']  # 获得正确答案的位置信息(中心位置)
        else:
            result = [555, 1147]
        # print(result)
        x, y = get_xp(result)  # 将位置信息用像素表示(实际位置):已随机处理
        d.click(x, y)
        time.sleep(random.uniform(3.8, 4))
        i += 1
        if i == 5:
            break

    # 退出
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(1.5, 2))
    # 回到'我要答题'界面
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(1.5, 2))


# 双人对战答题
def to_srdz(d):
    # 进入双人对战
    go_srdz(d)
    i = 0
    while 1:
        image = d.screenshot()
        image.save('hh.png')
        question = Model.do_image(a=70, b=670, c=1000, d=2175)  # 获取题目
        answer = get_answer(question)  # 寻找最优答案(A B C D)中的一个
        position = Model.matchImg('hh.png', '.\\image2\\zhengshangyou\\' + str(answer) + '.png')  # 匹配答案位置
        if position is not None:
            result = position['result']  # 获得正确答案的位置信息(中心位置)
        else:
            result = [555, 1147]
        # print(result)
        x, y = get_xp(result)  # 将位置信息用像素表示(实际位置):已随机处理
        d.click(x, y)
        time.sleep(random.uniform(4.7, 5.2))
        i += 1
        if i == 5:
            break

    # 返回
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(1.5, 2))
    # 回到'我要答题'界面
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    time.sleep(random.uniform(1.5, 2))
    # 点击确认退出界面
    d(text='退出').click(offset=(random.random(), random.random()))
    print("双人对战答题已完成")


# 合并
def zsydt(d):
    print("正在进入争上游答题模块\n\n")
    to_zsydt(d)  # 争上游答题
    to_zsydt(d, first=False)  # 每天答题两遍
    print("争上游答题模块已结束，正在进入双人对战\n\n")
    to_srdz(d)  # 双人对战
    # 回到'我的'
    time.sleep(random.random())
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
    # 回到主界面
    time.sleep(random.random())
    d(resourceId="com.android.systemui:id/back").click(offset=(random.uniform(0.3,0.6), random.uniform(0.3,0.6)))
