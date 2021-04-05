def solution(strings, n):
    mystring = list(list(st) for st in strings)
    mystring.sort(key = lambda mystring: (mystring[n], mystring))
    answer = list("".join(st) for st in mystring)
    return answer