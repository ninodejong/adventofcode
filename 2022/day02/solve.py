f = [x.split(" ") for x in open("input.txt").read().strip().split("\n")]

score_i = 0
score_o = 0
for r in f:
    o = r[1] # switch to 0 for part 1
    i = r[0]# switch to 1 for part 1
    
    if i == "X":
        if o == "C":
            score_i += 6
        if o == "A":
            score_i += 3
        score_i += 1

    if i == "Y":
        if o == "A":
            score_i += 6
        if o == "B":
            score_i += 3
        score_i += 2

    if i =="Z":
        if o == "B":
            score_i += 6
        if o == "C":
            score_i += 3
        score_i += 3
        
    #part 2
        
    if i == 'A':
        if o == 'X':
            score_o += (3)
        elif o == 'Y':
            score_o += (1 + 3)
        else:
            score_o += (2 + 6)
    elif i == 'B':
        if o == 'X':
            score_o += (1)
        elif o == 'Y':
            score_o += (2 + 3)
        else:
            score_o += (3 + 6)
    else:
        if o == 'X':
            score_o += (2)
        elif o == 'Y':
            score_o += (3 + 3)
        else:
            score_o += (1 + 6)
    
print(score_i)
print(score_o)