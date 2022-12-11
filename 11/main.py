from math import prod

with open('input.txt') as f:
    d = [x for x in f.read().split('\n\n') if x]

def parse(b):
    data = {(k:=a.strip().split(': '))[0]: k[1] for a in b.split('\n')[1:]}
    return {
        'items': [int(x) for x in data['Starting items'].split(', ')],
        'op': data['Operation'].split(' ')[-2:],
        'div_by': int(data['Test'].split(' ')[-1]),
        'throw_to': [int(data[f'If {x}'].split(' ')[-1]) for x in ['false', 'true']],
        'insp': 0
    }

def rounds(n, div):
    mks = [parse(x) for x in d]
    s = prod([x['div_by'] for x in mks])
    for _ in range(n):
        for m in mks:
            while len(m['items']):
                item, [op, val] = m['items'].pop(0), m['op']
                t = (item*(int(val) if val.isnumeric() else item) if op=='*' else item+int(val))//div
                m['insp'] += 1
                mks[m['throw_to'][t % m['div_by'] == 0]]['items'].append(t % s)
    return prod(sorted([m['insp'] for m in mks])[-2:])

print(rounds(20, 3), rounds(10000, 1), sep='\n')