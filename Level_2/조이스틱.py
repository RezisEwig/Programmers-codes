def solution(name):
    answer = 0
    index = 0
    combo = 0
    max_combo = 0
    list_name = list(name)
    
    for i in range(len(list_name)):
        if list_name[i] == 'A':
            combo += 1
        else :
            combo = 0
            
        if max_combo < combo :
            index = i
            max_combo = combo
        
        diff = ord(list_name[i]) - ord('A')
        if diff >= 13 :
            diff = (diff - 26) * (-1)
        
        answer += diff
    
    if index - max_combo < max_combo :
        answer += len(name)-1 + index - 2*max_combo
    else :
        answer += len(name)-1
    
    return answer