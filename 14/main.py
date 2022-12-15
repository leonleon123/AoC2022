from functools import reduce

from numpy import array, linspace

d = [array([array([int(x) for x in y.split(',')]) for y in l.split('->')]) for l in open('input.txt').read().splitlines()]
walls = reduce(lambda a,b: a|b, [set(tuple(x) for x in linspace(p1,p2,max(abs(p2-p1))+1)) for p in d for p1,p2 in zip(p,p[1:])])
my = max(max(x[:,1]) for x in d)

def fall(a, w):
    p = array([500, 0])
    while 1:
        if p[1] >= my + a:
            if a > 0:
                w.add(tuple(p))
                break
            else:
                return True
        for c in [[0,1], [-1,1], [1,1]]:
            if tuple(p + c) not in w:
                p += c
                break
        else:
            w.add(tuple(p))
            break
    return tuple(p) == (500,0)

def simulate(a):
    ol, w = len(walls), set(walls)
    while not fall(a,w): pass
    return len(w) - ol

print(simulate(0),simulate(1),sep='\n')