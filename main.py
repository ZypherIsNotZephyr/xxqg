"""
function 学习强国自动化测试
from 冬眠的int21h
made by 2021.1.24
"""
import function1
import function3
import function4
import Model
import uiautomator2 as u2


def xxqg():
    d = u2.connect_usb('71c60eef')  # 本机标识
    # 启动学习强国
    Model.setup(d)
    # 挑战答题
    function1.tzdt(d)
    # 争上游答题 双人对战
    function4.zsydt(d)
    # # 视听学习模块
    # function3.stxx(d)


if __name__ == '__main__':
    xxqg()
