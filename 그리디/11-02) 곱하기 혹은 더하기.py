n = input()
count=0
result = int(n[0])


for i in n[1:]:
    if result<=1 or int(i)<=1:
        result += int(i)
    else:
        result *= int(i)

print(result)


# 02984