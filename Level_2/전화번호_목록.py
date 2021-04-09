def solution(phone_book):
    phone_book.sort()
    for k, v in enumerate(phone_book[:-1]):
        if v == phone_book[k+1][:len(v)] :
            return False
    
    return True