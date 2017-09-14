#!/usr/bin/python
# -*- coding: UTF-8 -*- 10
import math
def kk(m):
    return int(math.log(m,2));

def coin(num,k,list):
 mk=kk(num);
 if mk>k:
        mk=k;
 if mk >= 0:
    num1=num-2*int(2**mk);
    if num1>0:
        coin(num1,mk-1,list);
    if num1==0:
        list.append(1)
    num2=num-int(2**mk);
    if num2>0:
        coin(num2,mk-1,list);
    if num2==0:
        list.append(1)
    if mk>0:
        coin(num,mk-1,list);
    return list
while(1):
    n=input("请输入：")
    if n<=0 :
        print "please input positive integer";
        continue;
    ink=kk(n);
    inlist=[];
    outlist=coin(n,ink,inlist);
    sum=len(outlist);
    print sum;
