numVotes = int(input())
votes = input()
numA = 0
numB = 0
for vote in votes:
    if vote == 'A':
        numA += 1
    else:
        numB += 1

if numA > numB:
    print('A')
elif numA < numB:
    print('B')
else:
    print("Tie")
