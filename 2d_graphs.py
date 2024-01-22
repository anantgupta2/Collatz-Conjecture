import matplotlib.pyplot as plt
##def coll_conj(a,j):
##    lst=[]
##    k=0
##    cycle=[43,5,11,17,221,253,187]
##    d=0
##    h=0
##    while True:
##        #if a<=len(lst1):
##         #   return(lst1[a-1])
##
##        if a in cycle:
##            d=cycle.index(a)
##            cyc=cycle[d]
##            return cyc
##        elif a%2==0:
##            a=a//2
##        else:
##            a=(3*a+j)//2
##        
##def mapper(input1,input2):
##    j=187
##    lst=[0,0,0,0,0,0,0]
##    for i in range(input1,input2+1):
##        a=coll_conj(i,j)
##        if a==5:
##            lst[0]+=1
##        elif a==11:
##            lst[1]+=1
##        elif a==17:
##            lst[2]+=1
##        elif a==43:
##            lst[3]+=1
##        elif a==221:
##            lst[5]+=1
##        elif a==253:
##            lst[6]+=1
##        else:
##            lst[4]+=1
##    tot=input2+1-input1
##    return [100*(lst[0]+lst[3])/tot,100*(lst[1]+lst[6])/tot,
##            100*(lst[2]+lst[5])/tot,100*lst[4]/tot]
##
##ctr=0
##lower=1
##upper=187
##a1=[]
##a2=[]
##a3=[]
##a4=[]
##a5=[]
##a6=[]
##a7=[]
##cycle=[[5,43],[11,253],[17,221],187]
##while ctr<200:
##    map_lst=mapper(lower,upper)
##    a1+=[map_lst[0]]
##    a2+=[map_lst[1]]
##    a3+=[map_lst[2]]
##    a4+=[map_lst[3]]
##    lower+=187
##    upper+=187
##    ctr+=1
##mst_lst=[a1,a2,a3,a4]
##
##for i in range(4):
##    plotter=mst_lst[i]
##    plt.figure(figsize=(32, 18))
##    plt.rc('xtick', labelsize=40)    # fontsize of the tick labels
##    plt.rc('ytick', labelsize=40)    # fontsize of the tick labels
##    plt.plot(plotter,'ro',color='blue')
##    plt.xlabel('Interval',fontsize=40)
##    str1='percentage of numbers mapped'
##    plt.ylabel(str1,fontsize=40)
##    str2='187_cycle_sum_'+str(cycle[i])+'int187.eps'
##    plt.savefig(str2,bbox_inches='tight')
##    str3='187_cycle_'+str(cycle[i])+'int187.png'
##    plt.savefig(str3)
##    plt.close()
##    print('saved')








def coll_conj(a,j,k=0):
    lst=[]
    p=0
    h=0
    while True:
##        if a<=len(lst1):
##            return(lst1[a-1])
        if a in lst:
            b=lst.index(a)
            c=lst[b:]
            return(min(c))
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(3*a+j)//2
        
def mapper(input1,input2):
    j=5
    lst=[0,0,0,0,0,0]
    for i in range(input1,input2+1):
        a=coll_conj(i,j)
        if a==19:
            lst[2]+=1
        elif a==5:
            lst[1]+=1
        elif a==1:
            lst[0]+=1
        elif a==23:
            lst[3]+=1
        elif a==187:
            lst[4]+=1
        elif a==347:
            lst[5]+=1
        else:
            lst[4]+=1
    tot=input2+1-input1
    return [100*lst[0]/tot,100*lst[1]/tot,100*lst[2]/tot,100*lst[3]/tot,100*lst[4]/tot,100*lst[5]/tot]

j=int(input("enter j"))
dict1=dict()
for i in range(1,10000):
    el=coll_conj(i,j)
    try:
        dict1[el]+=[i]
    except:
        dict1[el]=[i]
for i in dict1:
    print(j,i, dict1[i][0:6],sep=' & ',end='$\cdots$ \\ \n')
    
##while ctr<200:
##    map_lst=mapper(lower,upper)
##    a1+=[map_lst[0]]
##    a2+=[map_lst[1]]
##    a3+=[map_lst[2]]
##    a4+=[map_lst[3]]
##    a5+=[map_lst[4]]
##    a6+=[map_lst[5]]
##    lower+=500
##    upper+=500
##    ctr+=1
##mst_lst=[a1,a2,a3,a4,a5,a6]
##col=['red','blue','black','gray','darkblue','purple','drakgreen']
##for i in range(6):
##    plotter=mst_lst[i]
##    plt.figure(figsize=(32, 18))
##    plt.rc('axes', labelsize=30)
##    plt.plot(plotter,'ro',color=col[i])
##    plt.xlabel('Minimum of interval of 500k',fontsize=30)
##    str1='percentage of numbers mapped '+ str(cycle[i])
##    plt.ylabel(str1,fontsize=30)
##    str2='5_cycle_sum_'+str(cycle[i])+'int500k2.eps'
##    plt.savefig(str2,bbox_inches='tight')
##    str3='5_cycle_'+str(cycle[i])+'int500k2.png'
##    plt.savefig(str3)
##    plt.close()
##    print('saved')
