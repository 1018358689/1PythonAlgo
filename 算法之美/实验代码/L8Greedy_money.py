# -*- coding: utf-8 -*-
"""
  Created on Wed Mar  4 21:22:56 2020
  贪心算法求最小面值人民币的数量
  @author: 刘瑜等
  源代码文件是：L8Greedy_money.py
"""
def Find_Money(Consume):
    Select_money=[] #记录人民币的选择情况
    if Consume<=0:
        print('输入消费金额有误，请重新处理！')
        return []
    Moneys=[[10,5],[5,2],[50,8],[20,3],[100,4],[2,11],[1,7]]
    sort_moneys=sorted(Moneys,key=lambda one:one[0],reverse=False) #从小到大排序
    print('第一次人民币排序情况：',sort_moneys)
    one_money=sort_moneys[0]                 #选取面值最小的      
    while sort_moneys: 
        i=1
        while i<=one_money[1]:               #选取当前面值人民币的数量
            Consume=Consume-one_money[0]     #一次减一张人民币的面值
            print(i,Consume)
            if Consume<one_money[0] or i==one_money[1] :  
                Select_money.append([one_money[0],i]) #选择人民币结果记录
                if Consume<=0:               #消费的小额面值的人民币都准备好了
                    return Select_money      #返回人民币选择结果
                sort_moneys=sort_moneys[1:]   #删除最小面值
                print('新的人民币排序情况：',sort_moneys)
                if sort_moneys!=[]:
                    one_money=sort_moneys[0]      #选取面值最小的
                    break
                else:
                    print('三酷猫太会花钱了，手头资金不够！差%d元'%(Consume))
                    return Select_money
            i+=1
    return Select_money
consume=561    
select_end=Find_Money(consume)
if select_end!=[]:
    print('三酷猫花%d需要小额面值的人民币如下：'%(consume))
    print(select_end)
