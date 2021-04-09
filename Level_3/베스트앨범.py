def solution(genres, plays):
    answer = []
    n = len(genres)
    genre_names = set(genres)
    play_score = dict([x, 0] for x in genre_names)
    
    for i in range(n):
        play_score[genres[i]] += plays[i]
    
    play_score = list(play_score.items())
    play_score.sort(key = lambda play_score : play_score[1], reverse=True)
    
    for genre_name in play_score:
        first_index = -1
        first_plays = -1
        second_index = -1
        second_plays = -1
        
        for index in range(n):
            if genres[index] == genre_name[0]:
                if plays[index] > first_plays :
                    second_index = first_index
                    second_plays = first_plays
                    first_index = index
                    first_plays = plays[index]
                elif plays[index] > second_plays :
                    second_index = index
                    second_plays = plays[index]
                    
        answer.append(first_index)
        if second_index != -1 :
            answer.append(second_index)
        
    
    return answer