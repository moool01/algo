a = int(input())
cnt = 0

while True:
    if a%2==0:
        a = a*3+1
    else:
        a = a*2+2

    cnt += 1
    
    if a >= 1000:
        break

print(cnt)