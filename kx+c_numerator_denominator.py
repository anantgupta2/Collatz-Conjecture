import mylib as m
import math
import random as r
def coll_num(up,dn,k):
    if len(up)!=len(dn):
        raise Exception ('U and D must have same length')
    tot_sum=0
    pow_2=1
    pow_k=k**(sum(up))
    for i in range(len(up)):
        pow_k//=k**(up[i])
        iter_sum=pow_2*pow_k*(k**up[i]-2**up[i])
        pow_2*=2**(up[i]+dn[i])
        tot_sum+=iter_sum
    return(tot_sum)
def fact_coll(up,dn,k):
    c=coll_num(up,dn,k)
    c2=2**sum(up+dn)-k**sum(up)
    c2=c2*(k-2)
##    if c2<0:
##        raise Exception('No Cycle Exists')
    return(c,m.factor(c),c2,m.factor(c2))
def first_cycle(up,dn,k):
    c=fact_coll(up,dn,k)
    lst=[]
    prod=1
    for i in c[3]:
        if i not in c[1]:
            lst+=[i]
            prod*=i
        else:
            c[1].remove(i)
    t0=c[0]*prod//c[2]
    return (prod,lst,t0)

def ran_cycle(k):
    rand=r.randrange(1,15)
    u=[]
    d=[]
    for i in range(rand):
        u+=[r.randrange(1,4)]
        d+=[r.randrange(1,4)]
    sum_u=sum(u)
    sum_d=sum(d)
    if 2**(sum_u+sum_d)-k**sum_u <0:
        return(ran_cycle())
    c=first_cycle(u,d)
    return(rand,u,d,c[2],c[0])
def first_cycle_output(up,dn,k):
    a=first_cycle(up,dn,k)
    print(k,'x+',a[0],' is the first expression with the first cycle with these up and downs and '
          ,a[2],' is the first element of the cycle',sep='')
