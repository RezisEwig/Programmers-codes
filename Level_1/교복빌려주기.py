def solution(n, lost, reserve):
    student = [1]*(n+1)
    count = -1
    
    for i in lost:
        student[i] -= 1
        
    for i in reserve:
        student[i] += 1
        
    for i in range(1, n+1) :
        if student[i] == 2 :
            if student[i-1] == 0 :
                student[i] -= 1
                student[i-1] += 1
            elif i != n and student[i+1] == 0 :
                student[i] -= 1
                student[i+1] += 1
    
    for i in student :
        if i >= 1 : count += 1
    
    answer = count
    return answer