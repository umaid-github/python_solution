def diagonalDifference(arr):
    n=len(arr)
    d1,d2,i,j=0,0,0,n-1
    for k in range(n):
        d1+=arr[k][k]
    for k in range(n):
        d2+=arr[i][j]
        i+=1
        j-=1
    return abs(d1-d2)

def diagonaldifference(arr):
    n=len(arr)
    d1,d2=0,0
    for i in range(n):
        for j in range(n):
            if i==j:
                d1+=arr[i][j]
            if i==n-j-1:
                d2+=arr[i][j]
    return abs(d1-d2)
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    print(diagonaldifference(arr))
