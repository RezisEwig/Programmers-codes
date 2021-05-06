def solution(gems):
    counter = {gems[0] : 1}
    varience = len(set(gems))
    length = len(gems)
    left = 0
    right = 0
    best = [0, length]
    
    while left < length and right < length :
        if len(counter) == varience :
            if best[1] - best[0] > right - left :
                best[1] = right
                best[0] = left
            
            if counter[gems[left]] == 1 :
                del counter[gems[left]]
            else :
                counter[gems[left]] -= 1
            
            left += 1
            
        else :
            right += 1
            if right == length : break
            if counter.get(gems[right]) == None :
                counter[gems[right]] = 1
            else :
                counter[gems[right]] += 1
    
    best[0] += 1; best[1] += 1
    
    return best