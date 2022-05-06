# -*- coding: utf-8 -*-
"""
  Created on Mon Mar  10 20:59:57 2020
  用递归求全排
  注意:递归调用一次,在内存里开辟一块空间,临时存储当前执行代码的状态(入栈)
  @author: 刘瑜等
  源代码文件是：U7permutations.py
"""
import copy
s=[]
def perm(numbers, position, end):#position为当前行的移动比较下标位置,end为排列的数的个数
    if position == end:
        #print(numbers)
        return numbers
    else:
        for index in range(position, end): 
            numbers[index],numbers[position] =numbers[position],numbers[index]#交换两比较数
            r=perm(numbers, position+1, end)                                    #递归进行下一个数在子范围内的排序
            if r!=None:
                global s
                s.append(copy.deepcopy(r))
            #print('index=%d,pos=%d'%(index,position))                         #打印一轮排序的变化结果(i层次深度,p移动位置)
            numbers[index],numbers[position] =numbers[position],numbers[index] #递归,每一步恢复原先状态
    return 
#number= ['a','b','c']
#number= ['a','b']
number= [4,10,1,5]            
n=len(number)
perm(number, 0,n)
print('end',s)