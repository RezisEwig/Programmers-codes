def solution(n, edge):
    vertex = dict()
    visited = [0]*(n+1)
    for a, b in edge :
        vertex[a] = vertex.get(a, []) + [b]
        vertex[b] = vertex.get(b, []) + [a]
    
    search = [1]
    next_search = []
    visited[1] = 1
    count = 1
    
    while search :
        for i in search :
            for j in vertex[i] :
                if visited[j] == 0 :
                    visited[j] = count
                    next_search.append(j)
        
        if len(next_search) != 0 :
            answer = len(next_search)
        search = next_search
        next_search = []
        count += 1
        
    return answer