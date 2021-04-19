def dfs(numbers, target, sub_result, depth) :
    global answer
    
    if depth == len(numbers) :
        if target == sub_result :
            answer += 1
            return
        else : return
    
    dfs(numbers, target, sub_result+numbers[depth], depth+1)
    dfs(numbers, target, sub_result-numbers[depth], depth+1)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer