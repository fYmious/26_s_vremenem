file = open('26.txt')
K, N = int(file.readline()), int(file.readline())
print(K, N)
a = sorted([list(map(int, i.split())) for i in file])
k, np = 0, 0
yach = [-1] * K
for i in range(N):
    start, finish = a[i]
    for j in range(K):
        if start > yach[j]:
            yach[j] = finish
            k += 1
            np = j
            break

print(k, np + 1)
