n = int(input())
a = True

for i in range(2,n):
    if n%i ==0:
        a = False

if a:
    print("P")
else:
    print("C")