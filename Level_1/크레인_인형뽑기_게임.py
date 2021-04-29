def solution(board, moves):
    width = len(board)
    slots = list(list() for _ in range(width+1))
    basket = []
    answer = 0
    
    for i in board :
        for j in range(width) :
            if i[j] != 0 :
                slots[j+1].append(i[j])
    
    for i in moves :
        if len(slots[i]) != 0 :
            if len(basket) != 0 and basket[-1] == slots[i][0] :
                slots[i].pop(0)
                basket.pop()
                answer += 2
            else :
                basket.append(slots[i].pop(0))
    return answer