def solution(str1, str2):
    listA = []
    listB = []
    countA = 0
    countB = 0

    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha() :
            listA.append(temp.upper())

    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha() :
            listB.append(temp.upper())

    for k1, v1 in enumerate(listA):
        for k2, v2 in enumerate(listB):
            if v1 == v2 :
                countA += 1
                listB.pop(k2)
                break

    countB = len(listA) + len(listB)

    if countA == 0 and countB == 0 : 
        answer = 1
    else :
        answer = countA/countB

    return int(answer*65536)