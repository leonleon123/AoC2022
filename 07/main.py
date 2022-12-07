cwd, sizes = [], {}
for c in [x.strip() for x in open('input.txt').read().split("$ ") if x]:
    if c.startswith("cd"):
        dirname = c.split(" ")[-1]
        cwd = cwd + [dirname] if dirname != ".." else cwd[:-1]
    elif c.startswith("ls"):
        for t in [x.split(" ")[0] for x in c.split("\n")[1:] if x[0].isnumeric()]:
            for x in ["/".join(cwd[:i+1]) for i in range(len(cwd))]:
                sizes[x] = sizes[x]+int(t) if x in sizes else int(t)
print(sum(x for x in sizes.values() if x <= 100000))
print(min(x for x in sizes.values() if 70000000 - sizes["/"] + x >= 30000000))
