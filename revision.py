print(100*1.1**7)
height=1.72
weight=68.5
bmi=weight/height**2
print(bmi)
print(type(bmi))
print('ab'+'cd')
print('ab'+str(12))
#list contain more than one data types

fam = [['shabir', 1.72], ['babar', 1.70], ['bhola', 1.69]]
print(fam)
for member in fam:
	print(member)
print(type(fam))
print(fam[0])
print(fam[-1])
print(fam[1])
print(fam[:])
print(fam[:2])
#list manuplating
fam[2][1]=1.70
print(fam)
fam_ext=fam+[['dad', 1.56], ['mom', 1.45],['none', 1.89]]
print(fam_ext)
del(fam_ext[5])
x=fam_ext
y=list(x)
print(x)
print(fam_ext)
#functions
tallest=max(fam_ext)
print(tallest)
print(round(1.99))
print(round(1.68,1))
print(complex(5, 2))
one =[11.2, 12.3, 23]
two =[10.0, 23.0, 10.0, 10.0]
full=one+two
print(full)
full_sorted = sorted(full, reverse=True)
full_sorted1 = sorted(full, reverse=False)
print(full_sorted)
print(full_sorted1)
#list method
print(one.index(23))
print(two.count(10.0))
count_check='aaaaaaaaaaaabcd'
print(count_check.count('a'))
#string method
bro = 'shabir'
print(bro.capitalize())
print(bro.replace('s', 'c'))
fam_ext.append(['me', 1.89])
print(fam_ext)
print(bro.upper())
d= 'abcdd'
print(d.count('d'))
from numpy import array
b=array([1,2,3,4])
print(b*2) 
import math
a=math.pi*(.45**2)
print('area'+':'+str(a))
from math import radians
dist = 192500*radians(12)
#work on numpy package
height1=[1.99, 1.67, 1.78, 1.67]
weight1=[89.0, 56.9, 45.9, 88.89]
import numpy as np 
np_height1=np.array(height1)
np_weight1=np.array(weight1)
bmi=np_weight1/np_height1**2
print(bmi)
for m in bmi:
	print(m)
print(bmi[2])
print(dist)
print(bmi>21)
print(bmi<21)
print(bmi[1])
print(weight1.index(89.0))
np_2d=np.array([height1, weight1])
print(np_2d)
print(np_2d.shape)
print(np_2d[:][0])
print(np_2d[0,1])



