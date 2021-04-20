def solution(begin, target, words):
    answer = 0
    queue = [(begin, 0)]
    n = len(begin)
    words_len = len(words)
    visited = [0]*words_len
    
    while queue :
        temp = queue.pop(0)
        b_word = temp[0]
        depth = temp[1]
        
        for index in range(words_len) :
            if visited[index] == 0 :
                eq_num = 0
                
                for i in range(n) :
                    if words[index][i] == b_word[i] : eq_num += 1
                
                if eq_num == n-1 :
                    if words[index] == target : return depth+1
                    visited[index] = 1
                    queue.append((words[index], depth+1))
                
    return 0