##import csv
##f=open('coll_conj_table2.csv','w',newline='')
##record=csv.writer(f,delimiter=',')
import mylib as m
import random
def coll_conj2(a,j):
    lst=[]
    s=0
    es=0
    os=0
    while True:
        if a in lst:
            break
        elif a%2==0:
            es+=a
            lst.append(a)
            a=a//2
        else:
            os+=a
            lst.append(a)
            a=(3*a+j)//2
        s+=a
        print(a)
    print(s,sep='   ')
    print(os,es,sep='   ')
def coll_conj3(a,j,k=0):
    lst=[]
    p=0
    h=0
    while True:
        if a<=len(lst2):
            return(lst2[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]
            return(len(c),min(c),sum(c))
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)
def coll_conj(a,j,k=0):
    lst=[]
    p=0
    h=0
    while True:
        if a<=len(lst1):
            return(lst1[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]
            return(len(c),min(c),sum(c))
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
        #k=k+1
global lst1
global lst2
##record.writerow(list(range(1,200,2)))
##mst_lst=[]
##g=[]
mst_lst=[]
for k in range(1):
    coll_lst=[]
    coll_lst2=[]
    lst2=[]
    lst1=[]
    s=0
    a2=[]
    a_32=[]
#    j=random.randrange(10001,50000,2)
    j=32901
    dic={}
    dic3={}
    print(j)
    for i in range(1,100000,2):
        a=coll_conj(i,j)
        lst1+=[a]
        a_3=coll_conj3(i,j)
        if a not in coll_lst:
            coll_lst.append(a)
            a2.append(a[2])
            try:
                dic[a[2]]+=[a]
            except:
                dic[a[2]]=[a]
        if a_3 not in coll_lst2:
            coll_lst2.append(a_3)
            a_32.append(a_3[2])
            try:
                dic3[a[2]]+=[a_3]
            except:
                dic3[a[2]]=[a_3]
    for p in dic:
        l=dic[p]
        if len(l)>1:
            print(l[0], m.factor(l[0][2]))
            #coll_conj2(l[0][1],j)
            print(l[1])
            #coll_conj2(l[1][1],j)
    print('----')
    for p in dic3:
        f=dic3[p]
        if len(f)>1:
            print(f[0], m.factor(f[0][2]))
            #coll_conj2(f[0][1],j)
            print(f[1])
            #coll_conj2(f[1][1],j)
    print('----------------------------------------------------')











##    g.append(len(coll_lst))
##    mst_lst.append(coll_lst)
##record.writerow(g)
##for i in range(max(g)):
##    k=[]
##    for j in mst_lst:
##        try:
##            k.append(j[i])
##        except:
##            k.append(' ')
##    record.writerow(k)
#[13,37,47,59,95,101,175]
