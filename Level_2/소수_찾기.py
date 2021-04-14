import itertools

def solution(numbers):
    str_numbers = list(numbers)
    answer = 0
    num_set = set()
    
    for i in range(1, len(numbers)+1):
        permu_numbers = list(itertools.permutations(str_numbers, i))
        
        for num in permu_numbers:
            num = int("".join(num))
            num_set.add(num)
        
    for num in num_set:
        if num == 0 or num == 1 :
            continue
            
        if num == 2 or num == 3 :
            answer += 1
            continue
                
        for k in range(2, num//2+1):
            if num%k == 0 :
                break
            if k == num//2 :
                answer += 1
    
    return answer