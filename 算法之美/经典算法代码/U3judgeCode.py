# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:31:35 2019
    判断花括号是否匹配
@author: 刘瑜
源代码文件是：U3judgeCode.py
"""
Code='''int main()
{
    char asciiCode;
        for(asciiCode = 32;asciiCode < 127;asciiCode++)
   {
       cout << asciiCode << endl;
    }
    char select;
    LOOP:
    cout << "格式正确吗? \n";
    cin >> select;
    switch(select)
    {
        case 'Y':
            cout << "是的，正确。\n";
            break;
        case 'N':
            cout << "不知道呢！\n"; 
            break;
        default:
            goto LOOP;
    }
   rectangle rect1;
   rect1.area = rect1.getArea(3,5);
   cout << rect1.area << endl;
   circle circle1;
   circle1.area = circle1.getArea(2.0);
   cout << circle1.area << endl;
   return 0;}
}
'''
stack=[]
flag=True
for s in Code:
    if s=='{':
        stack.append(s)
    elif s=='}':
        if not stack:
            stack.pop()
        else:
            print("此段代码缺左花括号！")
            flag=False
            break
if not stack and flag:
    print('此段代码花括号匹配正确！')
else:
    print(stack)
    