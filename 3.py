input()
s = input()
d = []
for g in range(0, len(s)):
    for i in range(len(s), g, -1):
        s1 = s[g:i]
        s2 = s1[::-1]
        st = True
        for j in range(len(s1)):
            if s1[j] == s2[j]:
                st = False
        if st == True:
            d.append(len(s1))
d.sort(reverse=True)
print(d[0])