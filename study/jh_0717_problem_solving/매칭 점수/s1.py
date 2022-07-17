# 테스트케이스 9번 실패

def solution(word, pages):
    word = word.lower()
    W = len(word)
    P = len(pages)

    basic_points = []
    total_points = []
    urls = []
    references = []

    # 각 페이지의 기본점수 및 링크를 구한다.
    for page in pages:
        # 현재 url 구하기
        page = page.split('\n')
        url = page[3][43:].rstrip(' "/>')
        urls.append(url)

        body_end_idx = page.index('</body>')
        links = []
        basic_point = 0

        for i in range(6, body_end_idx):
            # 텍스트와 <a> 태그 분리
            page[i] = page[i].replace('<a href="', '\n').replace('</a>', '\n').replace('">', '\n')

            for line in page[i].split('\n'):
                # 링크인 경우
                if line.startswith('https'):
                    links.append(line[8:])
                # 텍스트인 경우
                else:
                    line = list(line)

                    for idx in range(len(line)):
                        if not line[idx].isalpha():
                            line[idx] = " "

                    for current in "".join(line).split(" "):
                        if current.lower() == word:
                            basic_point += 1

        references.append(links)
        basic_points.append(basic_point)
        total_points.append(basic_point)

    for idx in range(P):
        reference = references[idx]
        basic_point = basic_points[idx]
        link_count = len(reference)

        if link_count == 0:
            link_point = 0
        else:
            link_point = basic_point / link_count

        for url in reference:
            if url in urls:
                total_points[urls.index(url)] += link_point

    max_point = max(total_points)

    for idx, point in enumerate(total_points):
        if point == max_point:
            return idx
