import mylib as p
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


prime= p.prime(1000)

def coll_conj(a,j,k=0):
    lst=[]
    d=0
    h=0
    while True:
        if a<=len(lst1):
            return(lst1[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]
            ind=c.index(min(c))
            fin_lst=c[ind:]+c[:ind]
            return(fin_lst)
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
global lst1
mst_lst=[]
g=[]
fig=plt.figure()
ax=plt.axes(projection='3d')
for j in range(1,200,2):
    zline=j
    coll_lst=[]
    lst1=[]
    print(j,"is the no.")
    for i in range(1,100000,2):
        a=coll_conj(i,j)
        lst1+=[a]
        if a not in coll_lst:
            coll_lst.append(a)
            xline=list(range(1,len(a)+1))
            yline=a
            ax.plot3D(yline,xline,zline)
            print(max(a))
    g.append(len(coll_lst))
    mst_lst.append(coll_lst)
plt.show()


