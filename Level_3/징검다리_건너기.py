def solution(stones, k):
    left = 0
    right = 200000000
    answer = 0
    
    while left <= right :
        mid = (left + right) // 2
        combo = 0
        flag = 0
        
        for i in stones :
            if i <= mid :
                combo += 1
            else :
                combo = 0
            
            if combo >= k :
                flag = 1
                break
        
        if flag == 1 :
            answer = mid
            right = mid - 1
        else :
            left = mid + 1

    return answer