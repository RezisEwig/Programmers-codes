import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def dfs(x, a, tree, visited):
    global answer
    
    visited[x] = 1

    for y in tree[x]:
        if not visited[y]:
            a[x] += dfs(y, a, tree, visited)
    answer += abs(a[x])
        
    return a[x]

def solution(a, edges):
    global answer
    answer = 0
    
    if sum(a) != 0:
        return -1
    
    tree = defaultdict(list)
    
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)

    visited = [0] * len(a)
    
    dfs(0, a, tree, visited)
    return answer