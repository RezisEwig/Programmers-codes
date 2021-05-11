def solution(enroll, referral, seller, amount):
    reverse_tree = dict()
    money_dict = dict()
    money_dict["-"] = 0
    answer = []
    
    for i in range(len(enroll)) :
        reverse_tree[enroll[i]] = referral[i]
        money_dict[enroll[i]] = 0
    
    for i in range(len(seller)) :
        total = amount[i]*100
        name = seller[i]
        
        while reverse_tree.get(name) != None :
            up = int(total*0.1)
            money_dict[name] += total - up
            total = up
            name = reverse_tree[name]
            
    for i in range(len(enroll)) :
        answer.append(money_dict[enroll[i]])
        
    return answer