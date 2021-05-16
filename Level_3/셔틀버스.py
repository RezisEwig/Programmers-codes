def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        hour, minute = timetable[i].split(":")
        timetable[i] = [int(hour), int(minute)]
    
    timetable.sort(key = lambda timetable : (timetable[0], timetable[1]))
    
    index = 0
    queue = []
    hour, minute = 9, 0
    answer = ''
        
    for _ in range(n):
        while index < len(timetable) :
            if timetable[index][0] > hour :
                break
            if timetable[index][0] >= hour and timetable[index][1] > minute :
                break
                
            queue.append(timetable[index])
            index += 1
        
        if len(queue) >= m :
            if queue[m-1][1] == 0 :
                answer = [queue[m-1][0]-1, 59]
            else :
                answer = [queue[m-1][0], queue[m-1][1]-1]
            
            for i in range(m):
                queue.pop(0)
        
        else :
            answer = [hour, minute]
            queue = []
        
        minute += t
        
        if minute >= 60 :
            hour += minute//60
            minute = minute%60
            
    if answer[0] < 10 :
        answer[0] = "0" + str(answer[0])
    else :
        answer[0] = str(answer[0])
        
    if answer[1] < 10 :
        answer[1] = "0" + str(answer[1])
    else :
        answer[1] = str(answer[1])
        
    return answer[0] + ":" + answer[1]