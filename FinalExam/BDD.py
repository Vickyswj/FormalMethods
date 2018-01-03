# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:46:31 2018

@author: 陈彪
版权所有,翻版必究
"""

#解析这个布尔表达式对应的逻辑信息
'''定义一个符号用于表示非,例如#'''
formula='f=x1*x2+x1*x3+x2*x3+x3*#x4'
#找到标志位置=
flag=formula.find('=')+1

strs=formula[flag:].split('+')

#字符信息
alphabet=[]
for i in range(len(strs)):
    for j in range(len(strs[i].split('*'))):
        if(strs[i].split('*')[j] in alphabet):
            pass
        else:
            alphabet.append(strs[i].split('*')[j])


'''这个函数主要是为了获取到公式的一些基础信息,例如关键的字符信息,
然后找到了字符的个数信息,后边需要做一些相关的处理,例如关系,例如逻
辑相关操作业.
'''
def  getformula(formula):
    
    flag=formula.find('=')+1
    strs=formula[flag:].split('+')

    #字符信息
    alphabet=[]
    for i in range(len(strs)):
        for j in range(len(strs[i].split('*'))):
            if(strs[i].split('*')[j] in alphabet):
                pass
            else:
                alphabet.append(strs[i].split('*')[j])
    return alphabet
        
        
'''这里需要做的是使用公式的解析出来结果信息,主要是模拟香农展开的操作'''

formula

flag=0 #这个标签主要是为了进行标识的信息,输出的参数是0或者是1
x='x4'

strs=formula[formula.find('=')+1:].split('+')

#假如存在这个字符串,然后进行判断,否则的话不做操作

strs1=''
for i in range(len(strs)):
    #i=3
    if(x in strs[i]):
        if('#' in strs[i]):
            x='#'+x
            flag=1-flag
            if(flag==1):
                strss=strs[i].split('*')
                id=strs[i].split('*').index(x)
                del strss[strs[i].split('*').index(x)]
                strs[i]=strss[0]
            elif(flag==0):
                strs[i]=None
        else:
            if(flag==1):
                strss=strs[i].split('*')
                id=strs[i].split('*').index(x)
                del strss[strs[i].split('*').index(x)]
                strs[i]=strss[0]
            elif(flag==0):
                strs[i]=None
    else:
        pass
    
for i in range(len(strs)-1):
    if(strs[i]==None):
        pass
    else:
        strs1+=strs[i]+'+'

strs1+=strs[-1]

'''这个函数主要是为了进行BDD图像的计算,核心点在香农展开式上,输入的
formula是字符串表达的公式,flag是0或者是1,x是给定的字符串,这个一定
需要在formula中
'''
def Shannon(formula,flag,x):
    
    strs=formula[formula.find('=')+1:].split('+')
    #假如存在这个字符串,然后进行判断,否则的话不做操作
    formulas=''
    for i in range(len(strs)):
        if(x in strs[i]):
            if('#' in strs[i]):
                x='#'+x
                flag=1-flag
                if(flag==1):
                    strss=strs[i].split('*')
                    del strss[strs[i].split('*').index(x)]
                    strs[i]=strss[0]
                elif(flag==0):
                    strs[i]=None
            else:
                if(flag==1):
                    strss=strs[i].split('*')
                    del strss[strs[i].split('*').index(x)]
                    strs[i]=strss[0]
                elif(flag==0):
                    strs[i]=None
        else:
            pass
        
    for i in range(len(strs)-1):
        if(strs[i]==None):
            pass
        else:
            formulas+=strs[i]+'+'
    
    formulas+=strs[-1]
    
    return formulas
        

#做了这个操作之后就应该生成一条路径



def mulhcars(num,x1,formula):
    if num==1:
        return formula
    elif num==0:
        return 0
    
    
    
'''
    
import pygraphviz as pgv

A=pgv.AGraph(directed=True,strict=True)
A.add_edge(1,2)
A.add_edge(1,3)
A.add_edge(2,4)
A.add_edge(2,5)
A.add_edge(5,6)
A.add_edge(5,7)
A.add_edge(3,8)
A.add_edge(3,9)
A.add_edge(8,10)
A.add_edge(8,11)
A.graph_attr['epsilon']='0.001'
print (A.string()) # print dot file to standard output
A.write('fooOld.dot')
A.layout('dot') # layout with dot
A.draw('fooOld.png') # write to file
    
'''