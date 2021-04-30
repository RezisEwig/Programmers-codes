def solution(s):
    storage = list()
    index = 0
    answer = []
    
    for token in s.split("},"):
        storage.append(list())
        for t in token.split(","):
            storage[index].append(int(t.replace("{", "").replace("}", "")))
        index += 1
    
    storage.sort(key = lambda storage : len(storage))
    
    for sss in storage :
        for s in sss :
            if s not in answer : 
                answer.append(s)
                break
    
    return answer