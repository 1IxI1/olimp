rectx, recty, k = (int(x) for x in input().split())
xes = []
yes = []
lines = []

for i in range(0,k):
    x, y = (int(l) for l in input().split())
    xes.append(x)
    yes.append(y)

S = x * y
v = S-k

for yk in range(1, recty+1): # going by y
    pos = 1
    for xk in range(1, rectx+1):
        for h in xes:
            if xk == h:
                if pos != 1:
                    lines.append(pos-1)
                    print('21. added ' + str(pos-1))
                    pos = 1
            else: pos+=1
    if pos != 1:
        print('25. added ' + str(pos-1))
        lines.append(pos-1)

print(lines)