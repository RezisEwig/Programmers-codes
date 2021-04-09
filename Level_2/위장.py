def solution(clothes):
    closet = dict()
    result = 1

    for c in clothes :
        try:
            closet[c[1]].append(c[0])
        except:
            closet[c[1]] = [c[0]]

    for c in closet.items():
        result *= len(c[1])+1

    return result-1