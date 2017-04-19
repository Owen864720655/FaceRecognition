# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: AllData.py
@time: 2016/7/15 10:42
@contact: ustb_liubo@qq.com
@annotation: AllData : 一次读入所有数据
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='AllData.log',
                    filemode='a+')

if __name__ == '__main__':
    pass
