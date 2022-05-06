# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:41:50 2019
传统算法和高空间利用率算法的比较
@author: 刘瑜等
源代码文件：U1_ShowCards.py
"""
#传统方法54张牌，随机抽取5张
Poker=['黑A','黑2','黑3','黑4','黑5','黑6','黑7','黑8','黑9','黑10','黑J','黑Q','黑K',
      '红A','红2','红3','红4','红5','红6','红7','红8','红9','红10','红J','红Q','红K',
      '梅A','梅2','梅3','梅4','梅5','梅6','梅7','梅8','梅9','梅10','梅J','梅Q','梅K',
      '方A','方2','方3','方4','方5','方6','方7','方8','方9','方10','方J','方Q','方K',
      '小王','大王']
print('一副牌有%d张'%(len(Poker)))
import random
Show=random.sample(Poker,5)        #随机抽取5张，展现
print(Show)
#=========================高空间利用率算法
'''
   这里默认规则为黑A到黑K顺序编号为1到13，红A到红K编号为14到26，梅A到梅K编号为27到39，
   方A到方K编号为40到52，小王编号53，大王编号54
'''
shape=['J','Q','K','小王','大王']
Show1=[]
Show2=[]
def getCards(name,r,Show2,shape=None):      #从同一花色13张牌里取一张牌
    if r==1 : 
        Show2.append(name+'A')
    elif r<=10:
        Show2.append(name+str(r))
    else:
        Show2.append(name+shape[r-11])  #考虑J、Q、K
   

for x in range(5):                #随机抽取5个值
    y=random.randint(1,55)        #在[1,54]范围里随机抽取一个整数
    Show1.append(y)
for r in Show1:                   #确定5张牌
    if r<=13:                     #取黑桃里的13张牌
       getCards('黑',r,Show2,shape)
    elif r>13 and r<=26:          #取红桃里的13张牌
       getCards('红',r-13,Show2,shape) 
    elif r>27 and r<=39:          #取梅花里的13张牌
       getCards('梅',r-26,Show2,shape)  
    elif r>40 and r<=52:          #取方块里的13张牌
       getCards('方',r-39,Show2,shape)
    else:
        Show2.append(shape[r%50])  #取小王或大王
print(Show2)                       #取出的5张牌
        
        
