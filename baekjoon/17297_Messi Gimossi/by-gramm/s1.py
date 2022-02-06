
def find_word(i, target):
    """
    messi(i)에서 target번째 인덱스의 문자를 찾는다.

    messi(i) = messi(i - 1) + 공백 문자 + messi(i - 2)
    """
    if i < 3:
        STRING = "Messi Gimossi"
        return STRING[target]

    # messi(i)의 왼쪽 부분인 messi(i - 1)에서 다시 탐색을 진행한다.
    if target < messi_length[i - 1]:
        return find_word(i - 1, target)
    # messi(i - 1)과 messi(i - 2) 사이의 공백 문자이므로, Messi Messi Gimossi를 리턴한다.
    elif target == messi_length[i - 1]:
        return " "
    # messi(i)의 오른쪽 부분인 messi(i - 2)에서 다시 탐색을 진행한다.
    else:
        return find_word(i - 2, target - messi_length[i - 1] - 1)


M = int(input())

"""
f(n)을 messi(n)의 길이라고 할 때,

f(1) = 5
f(2) = 13
f(n) = f(n - 1) + f(n - 2) + 1
"""
messi_length = [0, 5, 13]  # messi_length[i]: messi(i)의 길이

while True:
    current = messi_length[-1] + messi_length[-2] + 1
    messi_length.append(current)

    if current >= M:
        break

result = find_word(len(messi_length) - 1, M - 1)

if result == " ":
    print("Messi Messi Gimossi")
else:
    print(result)
