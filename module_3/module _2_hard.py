n = int(input())
result = ''
for i in range(1, n):
    for j in range(i+1, n):
        if n % (j + i) == 0:
            result = result + str(i) + str(j)
print(result)