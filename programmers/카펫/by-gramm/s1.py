def solution(brown, yellow):
    # brown + yellow = width * height
    # brown = 2 * (width + height) - 4
    wh = brown + yellow

    for h in range(1, wh + 1):
        if wh % h == 0:
            w = wh // h
            if 2 * (w + h) - 4 == brown:
                return [w, h]
