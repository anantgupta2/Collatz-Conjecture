import mylib as m
import random as r
def coll_num(up,dn):
    if len(up)!=len(dn):
        raise Exception ('l1 and l2 must have same length')
    tot_sum=0
    pow_2=1
    pow_3=3**(sum(up))
    for i in range(len(up)):
        pow_3//=3**(up[i])
        iter_sum=pow_2*pow_3*(3**up[i]-2**up[i])
        pow_2*=2**(up[i]+dn[i])
        tot_sum+=iter_sum
    return(tot_sum)
def fact_coll(up,dn):
    k=coll_num(up,dn)
    k2=2**sum(up+dn)-3**sum(up)
    return(k,m.factor(k),k2,m.factor(k2))
def first_cycle(up,dn):
    k=fact_coll(up,dn)
    lst=[]
    prod=1
    for i in k[3]:
        if i not in k[1]:
            lst+=[i]
            prod*=i
        else:
            k[1].remove(i)
    t0=k[0]*prod//k[2]
    return (prod,lst,t0)

def ran_cycle():
    rand=r.randrange(1,15)
    u=[]
    d=[]
    for i in range(rand):
        u+=[r.randrange(1,4)]
        d+=[r.randrange(1,4)]
    sum_u=sum(u)
    sum_d=sum(d)
    if 2**(sum_u+sum_d)-3**sum_u <0:
        return(ran_cycle())
    k=first_cycle(u,d)
    return(rand,u,d,k[2],k[0])
def first_cycle_output(up,dn):
    a=first_cycle(up,dn)
    print(3,'x+ (',a[0],') is the first expression with the first cycle with these up and downs and '
          ,a[2],' is the first element of the cycle',sep='')























##import csv
##import statistics as s
##f=open('coll_conj_last_ 12.csv','w',newline='')
##record=csv.writer(f,delimiter=',')
##
##
##        
##def coll_conj(a,j,k=0):
##    lst=[]
##    u=0
##    d=0
##    while True:
##        if a<=len(lst1):
##            new=lst1[a-1]
##            new+=len(lst)-1
##            return(new)
##        elif a in lst:
##            return(len(lst))
##        elif a%2==0:
##            lst.append(a)
##            a=a//2
##        else:
##            lst.append(a)
##            a=(3*a+j)//2
##global lst1
##record.writerow(['k','max','max value','min','min value','median','average'])
##
##mst_lst=[]
##g=[]
##record_lst=[]
##for j in range(1,200,2):
##    coll_lst2=[]
##    coll_lst=[]
##    lst1=[]
##    print(j)
##    for i in range(1,1000000):
##        a=coll_conj(i,j)
##        lst1+=[a]
##    max1=max(lst1)
##    min1=min(lst1)
##    append_lst=[j,max1,lst1.index(max1),min1,lst1.index(min1),s.median(lst1),s.mean(lst1)]
##    record.writerow(append_lst)
##f.close()
