import csv
f=open('coll_conj_neg_ 2.csv','w',newline='')
record=csv.writer(f,delimiter=',')


        
def coll_conj(a,j,k=0):
    lst=[]
    u=0
    d=0
    while True:
        if a<=len(lst1) and a>0:
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
for j in range(1,200,2):
    coll_lst2=[]
    coll_lst=[]
    lst1=[]
    print(j)
    for i in range(-99999,100000,2):
        a=coll_conj(i,j)
        lst1+=[a]
        if a not in coll_lst:
            append_lst=list(a[:6])+a[6]
            record.writerow(append_lst)
            coll_lst.append(a)
            print("reached")
f.close()
