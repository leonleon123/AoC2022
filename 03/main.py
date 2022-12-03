d, p = [x for x in open('input.txt').read().split('\n') if x],lambda s: sum(ord(y)-ord('a')+1 if y.islower() else ord(y)-ord('A')+27 for y in s)
print(sum(p(set(x[:len(x)//2])&set(x[len(x)//2:])) for x in d),sum(p(set(a)&set(b)&set(c)) for a,b,c in [d[i:i+3] for i in range(0,len(d),3)]),sep='\n')
