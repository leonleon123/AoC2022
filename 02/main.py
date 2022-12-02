d = [[["ABC", "XYZ"][i].index(y) for i, y in enumerate(x.split(' '))] for x in open('input.txt').read().split('\n') if x]
print(sum(b + 1 + ((b == (a + 1) % 3)*2 + (a == b)*1) * 3 for a, b in d), sum((a - [1, 0, -1][b]) % 3 + 1 + b*3 for a, b in d), sep='\n')
