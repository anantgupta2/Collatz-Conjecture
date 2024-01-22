import csv
name=input('Enter name of the file(.csv at the end):')
f=open(name,'w',newline='')
record=csv.writer(f,delimiter=',')
def coll_conj(a,k):
    lst=[]
    ctr=0
    while ctr<main_counter+1:
        if a in glob_lst:
            return(a)
        if a in lst:
            b=lst.index(a)
            min_el=min(lst[b:])
            glob_lst.append(min_el)
            return(min_el)
        elif a%2==0:
            lst.append(a)
            a=a//2
        else:
            lst.append(a)
            a=(k*a+1)//2
        ctr+=1
global glob_lst
global main_counter
main_counter=int(input("Enter the maximum iterations for one input:"))
start=int(input("Enter the starting value of k:"))
end=int(input("Enter the ending value of k:"))
iterations=int(input("Enter the value you want to check till:"))
for k in range(start,end+1,2):
    glob_lst=[]
    for a in range(1,iterations+1,2):
        coll_out=coll_conj(a,k)
        print(k,glob_lst)
    record.writerow([k]+glob_lst)
    print(k)
print('Done')      
f.close()        

























































