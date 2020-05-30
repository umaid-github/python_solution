def compareTriplets(a,b):
    res=[0,0]
    for i,j in zip(a,b):
        if i > j:
            res[0]+=1
        elif i < j:
            res[1]+=1
    return res

if __name__=='__main__':
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=compareTriplets(a,b)
    for i in res:
        print(i,end=" ")

    
