import csv
import random
import mylib as m
f=open('coll_conj_lastest.csv','w',newline='')

record=csv.writer(f,delimiter=',')
record.writerow(['k','tot. original cycles','max T_0'])
def hcf(a,b):
    if b>a:
        a,b=b,a
    while True:
        j=a%b
        if j==0:
            break
        a,b=b,j
    return(b)  
        
def coll_conj(a,j,k=0):
    lst=[]
    while True:
        if a<=len(lst1):
            return(lst1[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]
            stp=len(c)-1
            return(stp,min(c))
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
        
global lst1
mst_lst=[]
g=[]
lst=[333669,445419,449235,560975,636637,650389,699075,787369,814071,976257]

for j in range(1,100):
    coll_lst=[]
    lst1=[]
    ctr=0
    max_el=0
    p=random.randrange(10001,100000,2)
    while p%3==0:
        p=random.randrange(10001,100000,2)
    print(p)
    print(j)
    stp_lst=[]
    min_lst=[]
    for i in range(1,1000000,2):
        a=coll_conj(i,p)
        lst1+=[a]
        if a not in coll_lst:
            HCF=hcf(p,a[1])
            if HCF==1:
                ctr+=1
                if max_el<a[1]:
                    max_el=a[1]
            
            coll_lst.append(a)
            print("reached")
    record.writerow([p,ctr,max_el])
f.close()
