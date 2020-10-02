'''
Title     : Min and Max
Subdomain : Numpy
Language    : Python
Problem   : https://www.hackerrank.com/challenges/np-min-and-max/problem
Solved By : Amber Kakkar
'''
import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    temp = list(map(int,input().split()))
    ar.append(temp)
np_ar = numpy.array(ar)
print(numpy.max(numpy.min(np_ar,axis=1)))