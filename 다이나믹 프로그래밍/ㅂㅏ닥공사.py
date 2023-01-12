num = int(input())
d = [0] *num

d[1] = 1
d[2] = 3

for i in range(3,num):
    d[i] = (d[i-1] + d[i-2]*2)%796796


print(d[num])