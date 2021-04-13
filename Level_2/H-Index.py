def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i+1 >= c :
            if i+1 == c :
                return c
            else :
                return i
            
    return len(citations)