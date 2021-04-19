def dfs(n, computers, i):
    global visited
    
    for j in range(n) :
        if computers[i][j] == 1 and visited[j] == 0 :
            visited[j] = 1
            dfs(n, computers, j)
            
def solution(n, computers):
    global visited
    visited = [0]*n
    answer = 0
    
    for i in range(n):
        if visited[i] == 0 :
            visited[i] = 1
            answer += 1
            dfs(n, computers, i)
            
    return answer