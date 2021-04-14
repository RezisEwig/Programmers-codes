def solution(brown, yellow):
    for height in range(1, yellow//2+2):
        if yellow % height != 0 :
            continue

        width = yellow / height

        if (width + height) * 2 + 4 == brown :
            return [width+2, height+2]

    return 0