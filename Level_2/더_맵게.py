import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0] < K :

        try :
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
        except IndexError :
            return -1
        
        answer += 1            
    
    return answer