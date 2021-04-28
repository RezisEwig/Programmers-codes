def solution(n, results):
    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()
    
    for battle in results:
        wins[battle[0]].add(battle[1])
        loses[battle[1]].add(battle[0])
                
    for i in range(1, n+1):
        for winner in loses[i]:
            wins[winner].update(wins[i])

        for loser in wins[i]:
            loses[loser].update(loses[i])
            
    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1
    return cnt