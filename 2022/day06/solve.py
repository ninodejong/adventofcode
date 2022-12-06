f = open('input.txt').read()

# f = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

ans = 0

for i in range(len(f)):
    if len(set(f[i:i+4])) == 4:
        ans = i + 4
        break

print(ans)

# f = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
ans = 0
for i in range(len(f)):
    if len(set(f[i:i+14])) == 14:
        ans = i + 14
        break

print(ans)