def solution(m, n, puddles):
    queue = [(1, 1)]
    road_map = [[0]*(n+1) for _ in range(m+1)]
    road_map[1][1] = 1
    
    while queue :
        temp = queue.pop(0)
        x = temp[0]
        y = temp[1]
        
        if x != m and [x+1, y] not in puddles :
            road_map[x+1][y] += road_map[x][y]
            if (x+1, y) not in queue :
                queue.append((x+1, y))
        
        if y != n and [x, y+1] not in puddles :
            road_map[x][y+1] += road_map[x][y]
            if (x, y+1) not in queue :
                queue.append((x, y+1))

    return road_map[m][n]%1000000007