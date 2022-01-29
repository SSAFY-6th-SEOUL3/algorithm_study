"""
가독성을 높이기 위해 클래스를 정의하여 정렬함.
"""


from sys import stdin


class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.korean_score = int(kor)
        self.english_score = int(eng)
        self.math_score = int(math)


N = int(stdin.readline())
total_scores = []

for _ in range(N):
    name, kor, eng, math = stdin.readline().split()
    total_scores.append(Score(name, kor, eng, math))

total_scores.sort(key=lambda x: x.name)
total_scores.sort(key=lambda x: x.math_score, reverse=True)
total_scores.sort(key=lambda x: x.english_score)
total_scores.sort(key=lambda x: x.korean_score, reverse=True)

for info in total_scores:
    print(info.name)
