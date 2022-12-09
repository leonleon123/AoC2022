from numpy import array, sign

d = [((s:=x.split(' '))[0],int(s[1])) for x in open('input.txt').read().splitlines()]
def simulate(n):
    h,t,p = array((0,0)),[array((0,0)) for _ in range(n)],[set() for _ in range(n)]
    for dr, a in d:
        for _ in range(a):
            h += {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}[dr]
            for i in range(n):
                t[i] += sign(df) if any(abs(df:=(h if i==0 else t[i-1])-t[i])==2) else (0,0)
                p[i].add(tuple(t[i]))
    return len(p[-1])
print(*[simulate(i) for i in [1, 9]],sep='\n')