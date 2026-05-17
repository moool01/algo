n = int(input())

for i in range(1,101):
    n = n//i
    if 1>=n:
        break
print(i)