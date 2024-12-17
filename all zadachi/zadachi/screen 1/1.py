a = []
b = []
n = int(input())
for i in range(n):
    a.append(int(input()))

for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)