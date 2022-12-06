import string

f = open("input.txt").read().strip().split("\n")

ascii = "." + string.ascii_lowercase + string.ascii_uppercase

score_1 = 0
score_2 = 0

for line in f:
    l, r = set(line[:len(line)//2]), set(line[len(line)//2:])
    i = list(l.intersection(r))[0]
    score_1 += (ascii.index(i))

for i in range(0, len(f), 3):
    a,b,c = set(f[i]), set(f[i+1]), set(f[i+2])
    i = list(a.intersection(b).intersection(c))[0]
    score_2 += ascii.index(i)

print(score_1)
print(score_2)