def coll_conj_print(a,j):
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
while True:
    try:
        a,j=tuple(map(int,input('Enter space separated a,k:').split()))
    except:
        break
    coll_conj_print(a,j)
