def get_melody_list(info):
    """
    Args:
        info: 멜로디의 문자열 리스트 (ex. 'ABC#DG#F')

    Returns:
        멜로디의 리스트 (ex. ['A', 'B', 'C#', 'D', 'G#', 'F'])
    """
    melodies = []
    melody_len = len(info)
    idx = 0

    while idx < melody_len - 1:
        if info[idx + 1] == '#':
            melodies.append(info[idx:idx + 2])
            idx += 2
        else:
            melodies.append(info[idx])
            idx += 1

    if idx == melody_len - 1:
        melodies.append(info[idx])

    return melodies


def solution(m, musicinfos):
    max_length, max_title = 0, "(None)"

    target_melodies = get_melody_list(m)
    TARGET_LEN = len(target_melodies)

    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(",")

        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        playtime = (end_h - start_h) * 60 + (end_m - start_m)

        if playtime <= max_length:
            continue

        current_melodies = get_melody_list(info)
        CURRENT_LEN = len(current_melodies)

        for i in range(playtime - TARGET_LEN + 1):
            for j in range(TARGET_LEN):
                if target_melodies[j] != current_melodies[(i + j) % CURRENT_LEN]:
                    break
            else:
                max_length = playtime
                max_title = title
                break

    return max_title
