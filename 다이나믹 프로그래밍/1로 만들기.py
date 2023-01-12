inputNum = int(input())

cashe = [0] * (inputNum+1)

for i in range(2, inputNum+1):
    cashe[i] = cashe[i-1]+1
    if i%2 == 0:
        cashe[i] = min(cashe[i], cashe[i//2]+1)
    if i%3 == 0:
        cashe[i] = min(cashe[i], cashe[i//3]+1)
    if i % 5 == 0:
        cashe[i] = min(cashe[i], cashe[i // 5] + 1)

print(cashe[inputNum])