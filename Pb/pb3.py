s, v, c, ok = input(), {'a', 'e', 'i', 'o', 'u'},'', 0
for x in s:
    c += x
    if x in v:
        c += '*'
        ok = 1
print(c if ok != 0 else "FARA VOCALE")