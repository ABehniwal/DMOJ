graph = {}
totalPaths = 0
bombs = []
visited = {}


def dfs(node,stop,graph,totalPaths,visited,currentVisited):
    
    if node == stop:
        for i in range(len(currentVisited)-1):
            visited[currentVisited[i]+currentVisited[i+1]] += 1
            totalPaths += 1
            
            return (totalPaths,visited,currentVisited)
            
    for nxt in graph[node]:
        if nxt not in currentVisited:
            currentVisited.append(nxt)
            a = dfs(nxt,stop,graph,totalPaths,visited,currentVisited)
            indx = currentVisited.index(nxt)
            currentVisited = currentVisited[:indx+1]

    return (totalPaths, visited, currentVisited)


connection = ''

while connection != '**':
    connection = input()
    if connection[0] not in graph:
        graph[connection[0]] = [connection[1]]
        
    else:
        graph[connection[0]].append(connection[1])
        
    if connection[1] not in graph:
        graph[connection[1]] = [connection[0]]
        
    else:
        graph[connection[1]].append(connection[0])
    visited[connection] = 0

currentVisited = ['A']

total,visited,currentVisited = dfs('A','B',graph,totalPaths, visited,currentVisited)


for i in visited:
    if visited[i] == totalPaths:
        bombs.append(i)


if len(bombs) == 0:
    print("There are 0 disconnecting roads.\n")
else:
    for i in bombs:
        print(i)
    print("There are " + str(len(bombs)) + " disconnecting roads.\n")
    
