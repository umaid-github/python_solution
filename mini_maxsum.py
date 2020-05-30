def miniMaxSum(arr):
    s=sum(arr)
    m=max(arr)
    mi=min(arr)
    print(s-m,s-mi,end=" ")
if __name__=='__main__':
    arr=list(map(int,input().split()))
    miniMaxSum(arr)
