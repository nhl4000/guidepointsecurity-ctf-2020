f = "FLAGGOESHERE"
a = []
for i in f:
    a.append(ord(i)-34)

print (a)


a = [37, 46, 49, 36, 42, 31, 37, 89, 15, 15, 35, 19, 16, 22, 65, 17, 15, 17, 63, 33, 14, 36, 67, 66, 34, 35, 14, 32, 22, 19, 18, 68, 64, 22, 22, 21, 64, 15, 14, 19, 91]
f = []
for i in range(len(a)):
    f.append(chr(a[i]+34))
print(''.join(f))
