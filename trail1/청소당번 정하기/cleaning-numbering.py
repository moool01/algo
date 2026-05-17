n = int(input())
cnt0 = 0
cnt1 = 0
cnt2 = 0
for i in range(1,n+1):
    if i%12 ==0:
        cnt2 +=1
    elif i%3 ==0:
        cnt1 += 1
    elif i%2 ==0:
        cnt0 +=1

print(cnt0,cnt1,cnt2)