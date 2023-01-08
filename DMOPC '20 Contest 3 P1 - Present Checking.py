n = int(input())
friends = list(map(int,input().split()))
num = {}
truth = True
for i in friends:
    if not i in num:
        num[i] = 1
    else:
        truth = False
        break
if truth:
    print("YES")
else:
    print("NO")
    



