def solution(priorities, location):
    answer = 0
    
    while priorities :
        paper = priorities.pop(0)
        flag = 0
        
        for i in range(len(priorities)) :
            if paper < priorities[i] :
                flag = 1
                break
                
        if flag == 1 :
            priorities.append(paper)
            location -= 1
            if location == -1 :
                location = len(priorities)-1
        else :
            answer += 1
            if location == 0 :
                return answer
            location -= 1