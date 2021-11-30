# from collections import Counter
#
# def solution(participant, completion):
#     print(Counter(participant))
#     print(Counter(completion))
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]
#
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

s = {12: 1, 28: 1, 878:1}
g = [1, 11, 1, 55, 12, 11, 14, 44] # movie_id
r = []

for genre_id, cnt in s.items(): # 12,1  28,1  878,1
    c = 0
    for i in range(len(g)):
        movie = Movie.objects.get(id=g[i])
        if genre_id in movie.genre_ids:
            r.append(movie)
            g.pop(i)
            c += 1
            if c == cnt:
                break
        else:
            # 동일 장르이면서 평점(vote_average)가 높은 영화
            alt = Movie.objects.filter(genre_ids__contains=genre_id).order_by('-vote_average')
            r.append()
            c += 1
            if c == cnt:
                break






