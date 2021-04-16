def check_finish(visited) :
    for i in visited :
        if i != 1 :
            return 1
    return 0


def solution(n, costs):
    visited = [0]*n
    index = 0
    costs.sort(key = lambda costs : costs[2])
    answer = 0
    area_code = 1

    while check_finish(visited) :

        if visited[costs[index][0]] == 0 and visited[costs[index][1]] == 0 :
            visited[costs[index][0]] = area_code
            visited[costs[index][1]] = area_code
            area_code += 1
            answer += costs[index][2]
            index += 1

        elif visited[costs[index][0]] == 0 or visited[costs[index][1]] == 0:
            visited[costs[index][0]] = max(visited[costs[index][0]], visited[costs[index][1]])
            visited[costs[index][1]] = visited[costs[index][0]]
            answer += costs[index][2]
            index += 1

        elif visited[costs[index][0]] != visited[costs[index][1]] :
            key = min(visited[costs[index][0]], visited[costs[index][1]])
            target = max(visited[costs[index][0]], visited[costs[index][1]])
            for i in range(n) :
                if visited[i] == target :
                    visited[i] = key
            answer += costs[index][2]
            index += 1

        else :
            index += 1

    return answer