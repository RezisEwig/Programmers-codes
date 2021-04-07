def solution(n):
    string = str(bin(n))[2:]
    print(string)
    count_0 = 0
    count_1 = 0
    index = 0
    
    for i in string :
        if i == '0' : count_0 += 1
        else : count_1 += 1
    
    
    if count_0 == 0 :
        answer_str = "10"+string[1:]
    else :
        while True :
            new_count_0 = 0
            new_count_1 = 0
            n = n+1
            string = str(bin(n))[2:]
            for i in string :
                if i == '0' : new_count_0 += 1
                else : new_count_1 += 1
                 
            if count_1 == new_count_1 :
                answer_str = string
                break
        

    answer = int(answer_str, 2)
    return answer