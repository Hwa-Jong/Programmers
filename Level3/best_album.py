# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    genres_set = set(genres)
    genres_dict = {gen: [0, []] for gen in genres_set}

    for idx in range(len(genres)):
        genres_dict[genres[idx]][0] += plays[idx]

        if len(genres_dict[genres[idx]][1]) >= 2:
                if genres_dict[genres[idx]][1][0][1] < plays[idx]:
                    genres_dict[genres[idx]][1].insert(0, [idx, plays[idx]])
                    genres_dict[genres[idx]][1] = genres_dict[genres[idx]][1][:2]

                elif genres_dict[genres[idx]][1][1][1] < plays[idx]:
                    genres_dict[genres[idx]][1].insert(1, [idx, plays[idx]])
                    genres_dict[genres[idx]][1] = genres_dict[genres[idx]][1][:2]   
                
        elif len(genres_dict[genres[idx]][1]) == 1:
                if genres_dict[genres[idx]][1][0][1] < plays[idx]:
                    genres_dict[genres[idx]][1].insert(0, [idx, plays[idx]])
                    genres_dict[genres[idx]][1] = genres_dict[genres[idx]][1][:2]
                else:
                    genres_dict[genres[idx]][1].insert(1, [idx, plays[idx]])
                    genres_dict[genres[idx]][1] = genres_dict[genres[idx]][1][:2]          
                
        else:
            genres_dict[genres[idx]][1].append([idx, plays[idx]])

    order = list(genres_dict.values())
    order.sort(key=lambda x: x[0], reverse=True)
    answer = []
    for i in range(len(order)):
        if len(order[i][1]) > 1:
            if order[i][1][0][1] < order[i][1][1][1]:
                answer.append(order[i][1][1][0])
                answer.append(order[i][1][0][0])
            else:
                answer.append(order[i][1][0][0])
                answer.append(order[i][1][1][0])
        else:
            answer.append(order[i][1][0][0])

    return answer