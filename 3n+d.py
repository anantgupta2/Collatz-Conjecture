##import csv
##f=open('coll_conj_table2.csv','w',newline='')
##record=csv.writer(f,delimiter=',')
##def coll_conj(a,j,k=0):
##    lst=[]
##    j=0
##    h=0
##    while True:
##        if a<=len(lst1):
##            return(lst1[a-1])
##        elif a in lst:
##            b=lst.index(a)
##            c=lst[b:]
##            for i in range(len(c)-1):
##                if c[i+1]>=c[i]:
##                    j=j+1
##                else:
##                    h=h+1
##            return(len(c),max(c),min(c))
##        elif a%2==0:
##            lst.append(a)
##            a=a//2
##        else:
##            lst.append(a)
##            a=(3*a+j)//2
##        #k=k+1
##global lst1
##record.writerow(list(range(1,200,2)))
##mst_lst=[]
##g=[]
##for j in range(1,200,2):
##    coll_lst=[]
##    lst1=[]
##    print(j)
##    for i in range(1,1000000,2):
##        a=coll_conj(i,j)
##        lst1+=[a]
##        if a not in coll_lst:
##            coll_lst.append(a)
##            print(a)
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




import math
