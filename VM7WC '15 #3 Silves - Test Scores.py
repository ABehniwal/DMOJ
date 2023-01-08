n,k = map(int,input().split())
scores = []
for i in range(n):
    scores.append(int(input()))
scores.sort()
maxScore = 0

for j in range(n-1,n-1-k,-1):
    if scores[j] <= 0:
        break
    else:
        maxScore += scores[j]

print(maxScore)
