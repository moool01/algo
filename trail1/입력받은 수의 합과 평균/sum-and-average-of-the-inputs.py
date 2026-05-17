n = int(input())
sum = 0 
cnt = 0
for i in range(n):
    a = int(input())
    cnt +=1
    sum += a


print(f'{sum} {sum/cnt:.1f}')