d = int(input('s len: '))
k = int(input('k: '))
ns = []
zeros = []
v = d - k

for i in range(0, k):
    ns.append(int(input()))
ns.sort(reverse=False)

if k == 1:
    l = ns[0]-1
    r = d-ns[0]
    if l > 1:
        zeros.append(l)
    if r > 1:
        zeros.append(r)

else:
    for i in range(0, k):
        if i == 0:
            l = ns[i]-1
            if l > 1:
                zeros.append(l)

        if i == k-1:
            l = ns[i] - ns[i-1] - 1
            r = d - ns[i]
            if r > 1:
                zeros.append(r)
            if l > 1:
                zeros.append(l)

        else:
            l = ns[i] - ns[i-1] - 1
            if l > 1:
                zeros.append(l)

for i in zeros:
    summ = 0
    for g in range(1, i):
        summ+=g
    v+=summ

print("") # TODO remove
print(v)
