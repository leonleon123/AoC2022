from numpy import array, flip, prod, sum, where

with open('input.txt') as f: d = array([[int(y) for y in x] for x in f.read().splitlines()])
print(4*len(d)-4+sum(array([any(max(x)<d[i,j] for x in [d[:i,j],d[i,:j],d[i+1:,j],d[i,j+1:]]) for i in range(1,len(d)-1) for j in range(1,len(d)-1)])))
print(max(prod(array([a[0]+1 if len(a:=where(x>=d[i,j])[0]) else len(x) for x in [flip(d[:i,j]),flip(d[i,:j]),d[i+1:,j],d[i,j+1:]]])) for i in range(1,len(d)-1) for j in range(1,len(d)-1)))