from numpy import array, where


def setup():
    d = array([[ord(y)-ord('a') for y in x] for x in open('input.txt').read().splitlines()])
    S, E = [tuple(x[0] for x in where(d == ord(i)-ord('a'))) for i in 'SE']
    d[S], d[E], m, n = 0, ord('z')-ord('a'), *d.shape
    return d, S, E, m, n, {(x,y): float('infinity') for x in range(m) for y in range(n)}

neighbours = lambda a: [tuple(x) for x in a[((a >= 0) & (a < (m, n))).all(axis=1)]]

def shortest(q, end):
    while len(q) > 0:
        dst, p = q.pop(0)
        if dst > dsts[p]: continue
        for i in neighbours(p + array([[1,0],[-1,0],[0,1],[0,-1]])):
            if (d[i] <= d[p] or d[i]-d[p] == 1) and dst+1 < dsts[i]:
                dsts[i] = dst + 1
                q.append((dst + 1, i))
    return dsts[end]

d, S, E, m, n, dsts = setup()
print(shortest([(0, S)], E), min(shortest([(0, x)], E) for x in zip(*where(d == 0))), sep='\n')
