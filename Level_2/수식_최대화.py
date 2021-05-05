import itertools

def solution(expression):
    expression = expression.replace("+", " + ")
    expression = expression.replace("-", " - ")
    expression = expression.replace("*", " * ")
    expression = expression.split()
    results = []
    priors = ["+", "-", "*"]
    priors = list(itertools.permutations(priors, 3))
    
    for p in priors :
        new_exp = expression.copy()
        flag = 1
        for t in range(3) :
            while True :
                try :
                    index = new_exp.index(p[t])
                except :
                    flag = 0
                    break
                
                new_exp[index-1] = "(" + new_exp[index-1] + new_exp[index] + new_exp[index+1] + ")"
                new_exp.pop(index)
                new_exp.pop(index)
        results.append(abs(eval(new_exp[0])))
    return max(results)