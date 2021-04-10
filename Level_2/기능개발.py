def release(progresses, speeds):
    count = 0
    while len(progresses) > 0 and progresses[0] >= 100 :
        count += 1
        progresses.pop(0)
        speeds.pop(0)
        
    return count

def solution(progresses, speeds):
    answer = []
    while progresses :
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if progresses[0] >= 100:
            answer.append(release(progresses, speeds))
            
    return answer