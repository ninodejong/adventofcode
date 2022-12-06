import re

f = open("input.txt").read()

rows = iter(f.splitlines())
stacks = [[] for i in range(10)]


def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))


for row in rows:
    if not row:
        break
    if row.startswith(" 1"):
        continue
    for i, c in enumerate(row[1::4]):
        if not c.isspace():
            stacks[i + 1].insert(0, c)

stacks2 = [s[:] for s in stacks]

for row in rows:
    count, fro, to = ints(row)

    for _ in range(count):
        stacks[to].append(stacks[fro].pop())

    stacks2[to].extend(stacks2[fro][-count:])
    stacks2[fro] = stacks2[fro][:-count]

print("".join(s[-1] for s in stacks[1:]))
print("".join(s[-1] for s in stacks2[1:]))
