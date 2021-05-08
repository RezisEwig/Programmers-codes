def isSafe(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def dfs(board, visited, vertical, x, y, sub_total):
    global answer, n, cost_map
    if sub_total > answer :
        return
    
    if x == n-1 and y == n-1 :
        if sub_total < answer :
            answer = sub_total
        return
            
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        newX, newY = x + dx[i], y + dy[i]
        if isSafe(newX, newY) and visited[newX][newY] == 0 :
            visited[newX][newY] = 1
            if i%2 == 0 :
                if vertical == 0 and cost_map[newX][newY] + 600 >= sub_total + 100:
                    cost_map[newX][newY] = min(cost_map[newX][newY], sub_total+100)
                    dfs(board, visited, 0, newX, newY, sub_total+100)
                elif cost_map[newX][newY] + 600 >= sub_total + 600 :
                    cost_map[newX][newY] = min(cost_map[newX][newY], sub_total+600)
                    dfs(board, visited, 0, newX, newY, sub_total+600)
            else :
                if vertical == 1 and cost_map[newX][newY] + 600 >= sub_total + 100:
                    cost_map[newX][newY] = min(cost_map[newX][newY], sub_total+100)
                    dfs(board, visited, 1, newX, newY, sub_total+100)
                elif cost_map[newX][newY] + 600 >= sub_total + 600 :
                    cost_map[newX][newY] = min(cost_map[newX][newY], sub_total+600)
                    dfs(board, visited, 1, newX, newY, sub_total+600)
            visited[newX][y + dy[i]] = 0
            
    
def solution(board):
    global answer, n, cost_map
    n = len(board)
    visited = board.copy()
    visited[0][0] = 1
    
    cost_map = list([float("inf")]*n for _ in range(n))

    answer = float("inf")
    dfs(board, visited, -1, 0, 0, 0)
    
    return answer - 500