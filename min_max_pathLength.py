import math
import csv
import statistics as s
f=open('coll_conj_random_ noln2.csv','w',newline='')
record=csv.writer(f,delimiter=',')


        
def coll_conj(a,j,k=0):
    lst=[]
    u=0
    d=0
    while True:
        if a<=len(lst1):
            new=lst1[a-1]
            new+=len(lst)-1
            return(new)
        elif a in lst:
            return(len(lst))
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
global lst1
record.writerow(['k','max','max value','median','average'])
g=[]
record_lst=[]
mst_lst=[449235, 787369, 976257, 650389, 560975, 814071, 445419, 333669, 636637, 699075]
for j in mst_lst:
    lst1=[]
    lst2=[]
    print(j)
    for i in range(1,1000000):
        a=coll_conj(i,j)
        lst1+=[a]
        
    max1=max(lst1)
    append_lst=[j,max1,lst1.index(max1)+1,s.median(lst1),s.mean(lst1)]
    record.writerow(append_lst)
f.close()
