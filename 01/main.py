print((d := sorted(sum(int(y) for y in x.split('\n')) for x in open('input.txt').read().split('\n\n')))[-1], sum(d[-3:]), sep='\n')
