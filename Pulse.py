n,s,t = map(int,input().split())
numWaves = 0
for i in range(n):
    wave = int(input())
    if 2*wave >= s and 2*wave <= t:
        numWaves += 1

print(numWaves)
