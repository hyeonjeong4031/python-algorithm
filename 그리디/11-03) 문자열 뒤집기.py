n = input()
count1 = 0
count0 = 0

if n[0] == "1":
    count0 += 1
else:
    count1 += 1

for i in range(1, len(n)):
    if n[i-1] != n[i]:
        if n[i] == 1:
            count0 += 1
        else:
            count1 += 1

print( min(count0, count1))