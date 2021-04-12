import heapq

def solution(jobs):
    jobs.sort(key = lambda jobs : jobs[0])
    heap = []
    time = 0
    answer = 0
    job_num = len(jobs)

    for i in range(job_num) :
        jobs[i][0], jobs[i][1] = jobs[i][1], jobs[i][0]

    while jobs or heap :

        while len(jobs) != 0 and jobs[0][1] <= time :
            heapq.heappush(heap, jobs.pop(0))

        if len(heap) == 0 :
            time += 1
            continue

        now = heapq.heappop(heap)
        answer += time - now[1] + now[0]
        time += now[0]


    return answer//job_num