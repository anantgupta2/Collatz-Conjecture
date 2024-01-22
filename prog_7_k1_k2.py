import csv
f=open('coll_conj_k1_k2_1.csv','w',newline='')
record=csv.writer(f,delimiter=',')
record.writerow(['j1','j2','stp','max','min','ups','downs'])

def coll_conj(inp,j1,j2):
        a=inp
        lst=[]
        d=0
        h=0
        k=True
        while True:
                print(a)
                if a in lst:
                    b=lst.index(a)
                    if lst[b-1]==lst[-1]:
                        
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
                        return(j1,j2,stp,max(c),min(c),smu,smd,stp_lst)
                    
                if a%2:
                    lst.append(a)
                    if k:
                        a=(3*a+j1)//2
                        k=False
                    else:
                        a=(3*a+j2)//2
                        k=True
                else:
                    lst.append(a)
                    a=a//2


for i in range(1,20,2):
    for j in range(1,20,2):
        coll_lst2=[]
        coll_lst=[]
        lst1=[]
        print(i,j)
        for k in range(-99999,100000,2):
            a=coll_conj(k,i,j)
            lst1+=[a]
            if a not in coll_lst:
                append_lst=list(a[:7])+a[7]
                record.writerow(append_lst)
                coll_lst.append(a)
                print("reached")
