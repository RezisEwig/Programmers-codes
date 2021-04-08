def delete(queue, num):
    index = 0
    max_v = 0
    min_v = float("inf")

    if len(queue) == 0 :
        return
    else :
        if num == 1 :
            for i in range(len(queue)):
                if queue[i] > max_v :
                    index = i
                    max_v = queue[i]
            queue.pop(index)
        else :
            for i in range(len(queue)):
                if queue[i] < min_v :
                    index = i
                    min_v = queue[i]
            queue.pop(index)

def insert(queue, num):
    queue.append(num)

def solution(operations):
    queue = []

    for i in operations:
        order, num = map(str, i.split())
        num = int(num)

        if order == "I" :
            insert(queue, num)
        else :
            delete(queue, num)

    if len(queue) == 0 :
        answer = [0,0]
    else :
        answer = [max(queue), min(queue)]

    return answer