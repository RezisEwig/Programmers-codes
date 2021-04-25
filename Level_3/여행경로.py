def dfs(visited, depth, start):
    global g_tickets, n, flag, answer
    if depth == n :
        flag = 1
        return
    
    for i in range(n) :
        if visited[i] == 0 and g_tickets[i][0] == start :
            answer.append(g_tickets[i][1])
            visited[i] = 1
            dfs(visited, depth+1, g_tickets[i][1])
            if flag != 0 : return
            answer.pop()
            visited[i] = 0

def solution(tickets):
    global g_tickets, n, flag, answer
    flag = 0
    g_tickets = tickets
    answer = ["ICN"]
    n = len(tickets)
    visited = [0]*n
    tickets.sort(key = lambda tickets : (tickets[1], tickets[0]))
    
    dfs(visited, 0, "ICN")
    return answer