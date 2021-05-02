def dfs(user_id, banned_id, depth, sub_set):
    global answer, n
    if depth == n :
        if sub_set not in answer :
            answer.append(sub_set.copy())
        return
    
    for u in user_id:
        if (u not in sub_set) and len(u) == len(banned_id[depth]) :
            for i in range(len(u)):
                if banned_id[depth][i] != u[i] and banned_id[depth][i] != "*" :
                    break
                if i == len(u) - 1 :
                    sub_set.add(u)
                    dfs(user_id, banned_id, depth+1, sub_set)
                    sub_set.remove(u)
    
def solution(user_id, banned_id):
    global answer, n
    user_id.sort(key = lambda user_id : len(user_id))
    banned_id.sort(key = lambda banned_id : len(banned_id))
    answer = []
    n = len(banned_id)
    
    dfs(user_id, banned_id, 0, set())
    
    return len(answer)