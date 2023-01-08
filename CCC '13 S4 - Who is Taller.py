from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
per1,per2 = map(int,sys.stdin.readline().split())

q = deque()
q.append(per1)
visited[per1] = True
q2 = deque()

smaller = 0

while q:
    node = q.pop()
    if node == per2:
        smaller = 2
        break
    for nxt in graph[node]:
        if not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True

if smaller == 0:
    visited = [False for i in range(n+1)]
    q2.append(per2)
    visited[per2] = True
    while q2:
        node = q2.pop()
        if node == per1:
            smaller = 1
            break
        for nxt in graph[node]:
            if not visited[nxt]:
                q2.append(nxt)
                visited[nxt] = True

if smaller == 0:
    print('unknown')
elif smaller == 1:
    print('no')
else:
    print('yes')

        

    
