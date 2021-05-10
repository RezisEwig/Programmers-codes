def solution(lines):
    time_table = []
    answer = 0
    for l in lines :
        _, t, s = l.split()
        hour, minute, sec = t.split(":")
        time = float(s[:-1])
        end = float(hour)*3600 + float(minute)*60 + float(sec)
        start = end - time + 0.001
        time_table.append([start, end])
        
    n = len(time_table)
    
    for i in range(n) :
        mark = time_table[i][1] + 1
        
        count = 0
        for j in range(i, n) :
            if mark > time_table[i][0] :
                count += 1
            i += 1
        
        if count > answer :
            answer = count
    
    return answer