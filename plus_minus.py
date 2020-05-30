def plusMinus(arr):
    n,p,z,s=0,0,0,len(arr)
    for i in arr:
        if i < 0:
            n+=1
        elif i > 0:
            p+=1
        else:
            z+=1
    ni = n/float(s)
    pi = p/float(s)
    zi= z /float(s)
    print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(pi,ni,zi))
if __name__=='__main__':
     n=int(input())
     arr=list(map(int,input().split()))
     plusMinus(arr)
