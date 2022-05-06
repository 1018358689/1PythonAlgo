# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:25:17 2019
    药店销售先进先出核算
@author: 刘瑜
源代码文件：U3FIFODrugstore.py
"""
InDetail=[['20191126001','阿莫西林',2,2,18],  #进货明细单
          ['20191126002','咳嗽糖浆',1,1,35],
          ['20191126003','小儿清肺片',10,10,35],
          ['20191126004','阿莫西林',5,5,19]]
SaleRecord=[[201911260001,'','阿莫西林',2,0,25],#销售明细单
            [201911260002,'','咳嗽糖浆',1,0,48],
            [201911260003,'','阿莫西林',1,0,25]]
i=0
s_len=len(SaleRecord)
while i<s_len :
    curr_Record=SaleRecord[i]
    j=0
    I_len=len(InDetail)
    while j<I_len :         #在进货表里获取进货编号、成本价、并削减实际数量
        if curr_Record[2]==InDetail[j][1] and  InDetail[j][3]>=curr_Record[3] :
            SaleRecord[i][1]=InDetail[j][0]      #获取入库编号
            SaleRecord[i][4]=InDetail[j][4]      #获取成本价
            InDetail[j][3]=InDetail[j][3]-SaleRecord[i][3]  #进货表减去销售数量
            break
        else:
            j+=1
    i+=1
print('处理后的销售表：')
for sale in SaleRecord:
    print(sale)
print('处理后的进货表：')
for Detail in InDetail:
    print(Detail)
