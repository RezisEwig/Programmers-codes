def solution(people, limit):
    people.sort()
    left = 0
    right = len(people)-1
    answer = 0
    
    while left <= right :
        if right-left == 0 :
            answer += 1
            break
        
        if people[left] + people[right] <= limit :
            answer += 1
            left += 1
            right -= 1
        else :
            answer += 1
            right -= 1
    
    return answer