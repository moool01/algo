n = int(input())
sum = 1
for i in range(1,101):
    sum *= i
    if sum>=n:
        break

print(i)