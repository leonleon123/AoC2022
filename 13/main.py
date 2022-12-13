from functools import cmp_to_key

d = [eval(x) for x in open('input.txt').read().split('\n') if x]
d1, p1, p2 = [d[i:i+2] for i in range(0,len(d),2)], [[2]], [[6]]

def cmp_pck(a, b):
    if type(a) == list and type(b) == list:
        for x, y in zip(a, b):
            if (v := cmp_pck(x, y)) != 'eq': return v
        if len(a) != len(b): return len(a) < len(b)
        return 'eq'
    elif type(a) != list and type(b) == list: return cmp_pck([a], b)
    elif type(a) == list and type(b) != list: return cmp_pck(a, [b])
    elif type(a) != list and type(b) != list: return 'eq' if a == b else a < b

print(sum((i+1)*cmp_pck(a, b) for i, [a, b] in enumerate(d1)))
print(((s:=sorted([*d, p1, p2], key=cmp_to_key(lambda a,b: 1-2*cmp_pck(a, b)))).index(p1)+1)*(s.index(p2)+1))