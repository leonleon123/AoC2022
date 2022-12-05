with open('input.txt') as file: s, m = file.read().split('\n\n')
s = [[y for y in x if y.strip()][::-1] for x in zip(*[[*x[1::4]] for x in s.split('\n')][:-1])]
def move(s,m,o):
    for a, src, dst in [[int(y) for y in x.split(' ')[1::2]] for x in m.split('\n') if x]:
        s[src-1][-a:],s[dst-1] = [],s[dst-1]+s[src-1][-a:][::o] 
    return ''.join([x[-1] for x in s])
print(*[move([[*x] for x in s],m,i) for i in [-1,1]],sep='\n')