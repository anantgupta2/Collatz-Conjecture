import csv
from mylib import prime

prime_lst=prime(1000)


f=open('coll_conj_single_cycle3.csv','w',newline='')
record=csv.writer(f,delimiter=',')
record.writerow(['k','total steps','max','min','up total','down total'])

def coprime(a,b):
    p=min(a,b)
    q=max(a,b)
    while q!=0:
        p,q=q,p%q
    if p==1:
        return True
    else:
        return False
def coll_conj(a,j,k=0):
    lst=[]
    u=0
    d=0
    while True:
        if a<=len(lst1):
            return(lst1[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]
            b=c.index(min(c))
            c=c[b:]+c[:b+1]
            stp=len(c)-1
            stp_lst=[]
            u=0
            d=0
            smu=0
            smd=0
            for i in range(stp):
                if c[i+1]>=c[i]:
                    u+=1
                    if d!=0:
                        stp_lst.append(d)
                    d=0
                    smu+=1
                else:
                    d+=1
                    if u!=0:
                        stp_lst.append(u)
                    u=0
                    smd+=1
            stp_lst.append(d)
                    
            return(j,stp,max(c),min(c),smu,smd,stp_lst)
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
global lst1
mst_lst=[]
g=[]
for j in prime_lst:
    coll_lst2=[]
    coll_lst=[]
    lst1=[]
    print(j)
    for i in range(1,1000000,2):
        a=coll_conj(i,j)
        lst1+=[a]
        if a not in coll_lst and coprime(j,a[3]):
            append_lst=list(a[:6])+a[6]
            coll_lst.append(a)
        if len(coll_lst)==2:
            break
    if len(coll_lst)==1:
        record.writerow(append_lst)
        print('ZIS')
        


f.close()
