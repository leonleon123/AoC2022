d = [((s:=x.split(' '))[0],int(s[1]) if len(s)>1 else 0) for x in open('input.txt').read().splitlines()]
c,x,s,o = 1,1,[],[['_']*40 for _ in range(6)]
for ins, a in d:
    for _ in range(1 if ins=='noop' else 2):
        s.append(x*c*(((c-20)%40)==0))
        o[(c-1)//40][(c-1)%40] = '.#'[((c-1)%40) in range(x-1,x+2)]
        c += 1
    x += a*(ins=='addx')
print(sum(s),*[''.join(x) for x in o], sep='\n')