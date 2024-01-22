import mylib
##f=open('coll_conj_stp_ 6.csv','w',newline='')
##record=csv.writer(f,delimiter=',')
import random
import mylib as p
def coll_conj(a,j,k=0):
    lst=[]
    d=0
    h=0
    while True:
        if a<=len(lst1):
            return(lst1[a-1])
        elif a in lst:
            b=lst.index(a)
            c=lst[b:]+[a]
            stp=len(c)-1
            for i in range(stp):
                if c[i+1]>=c[i]:
                    d=d+1
                else:
                    h=h+1
            return(stp,max(c),min(c),d,h)
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
global lst1
##record.writerow(list(range(1,200,2)))
mst_lst=[]
z=0
for j in range(1,200,2):
    coll_lst2=[]
    coll_lst=[]
    lst1=[]
    #print()
    #j=random.randrange(p_len)
    #j=prime_lst[j]
    
    for i in range(1,10000,2):
        a=coll_conj(i,j)
        lst1+=[a]
        if a not in coll_lst:
            coll_lst.append(a)
            if a[2]==i and i!=j:
                print(j)
                print(a[2],i)
                print(mylib.factor(i))
    print('\n\n')
##        if z==0:
##            z=1
##            break
##            print()
##    for i in coll_lst:
##        if i[2]%j==0:
##            coll_lst2.append(i)
##            print(i)
##    g.append(len(coll_lst2))
##    mst_lst.append(coll_lst2)
##record.writerow(g)
##for i in range(max(g)):
##    k=[]
##    for j in mst_lst:
##        try:
##            var=j[i]
##            k.append(var)
##        except:
##            k.append(' ')
##    record.writerow(k)
##f.close()
