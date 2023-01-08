import sys
sys.stdin.readline()

m,n,k = map(int,input().split())
singerNote = []
numParallel = 0

for i in range(m):
    n1 = list(input().split())
    singerNote.append(n1)
    

for i in range(m-1):
    for l in range(i+1,m):
        for j in range(n-1):
            if int(singerNote[i][j]) - int(singerNote[l][j]) == k:
                first = i
                second = l
                if int(singerNote[first][j+1]) - int(singerNote[second][j+1]) == k:
                    numParallel+=1
                
            elif int(singerNote[l][j]) - int(singerNote[i][j]) == k:
                first = l
                second = i
                if int(singerNote[first][j+1]) - int(singerNote[second][j+1]) == k:
                    numParallel += 1

print(numParallel)

