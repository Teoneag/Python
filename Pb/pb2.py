s = "aa"

while 1:
    ok = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            ok = 1
            break
    if ok == 0:
        break

print(s if (len(s) > 0) else "Empty String")
