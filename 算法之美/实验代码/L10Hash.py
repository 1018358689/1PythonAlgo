# -*- coding: utf-8 -*-
"""
  Created on Wed Feb 19 20:35:37 2020
  一般哈希算法,带冲突处理（仅处理1个冲突）
  @author: 刘瑜
  源代码文件是：U10hash.py
"""
records=[[1,5],[8,29],[15,20],[17,21],[31,60],[21,100]]  #数据键为日期序号，值为销售鱼数量
SAddress1={'192.168.1.1':5}                     #服务器1地址和数据存放地址
SAddress2={'192.168.1.2':10}                    #服务器2地址和数据存放地址
SAddress3={'192.168.1.3':15}                    #服务器3地址和数据存放地址
SAddress4={'192.168.1.4':20}                    #服务器4地址和数据存放地址

n=20                                            #销售记录长度，这里假设是20
for one in records:
    if one[0]%n<=SAddress1['192.168.1.1']:   #哈希值在0到5之间
        if SAddress1.get(one[0]%n)==None :         #地址没有冲突
            SAddress1[one[0]]=one[1]             #数据存放到服务器地址1上
        else :
            SAddress1[one[0]%n+1]=one[1]         #往后探一位存储
    elif one[0]%n<=SAddress2['192.168.1.2']: #哈希值在6到10之间
        SAddress2[one[0]]=one[1]             #数据存放到服务器地址2上 
    elif one[0]%n<=SAddress3['192.168.1.3']: #哈希值在11到15之间
        SAddress3[one[0]]=one[1]             #数据存放到服务器地址3上 
    elif one[0]%n<=SAddress4['192.168.1.4']: #哈希值在16到20之间
        SAddress4[one[0]]=one[1]             #数据存放到服务器地址4上 
print(SAddress1)                             #打印服务器1中的数据
print(SAddress2)                             #打印服务器2中的数据
print(SAddress3)                             #打印服务器3中的数据
print(SAddress4)                             #打印服务器4中的数据