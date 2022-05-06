# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:17:44 2019
求润年
@author: 刘瑜等
源代码文件：U2LeapYear.py
"""
def RunYear(y):
    if y%4==0 and y%100!=0 : #能被4整除，但不是百年的是润年
        return 1
    elif y%400==0 :           #能被400年整除的是润年
        return 1
    else:
        return 0             #不是润年
try:
    year=int(input('输入年份：'))
    if year>=0 :
        r1=RunYear(year)
        if r1 :
            print('%d是润年'%(year))
        else:
            print('%d不是润年'%(year))
    else:
        print('输入年份值不对！')
except:
    print('输入值有误！')
