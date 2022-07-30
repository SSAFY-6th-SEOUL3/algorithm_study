function solution(info, edges) {
    const N = info.length
    const parents = new Array(N + 1).fill(-1)
    const startLambs = []

    // 0으로 표시된 양 노드들을 (루트 노드를 제외하고) -1로 변환한다.
    for (let i = 1; i < N + 1; i++) {
        if (info[i] === 0) {
            info[i] = -1
            startLambs.push(i)
        }
    }

    for (let [a, b] of edges) {
        parents[b] = a
    }

    // 부모 노드 중 방문하지 않은 양 노드가 없는 양 노드를 후보로 삼는다.
    // 각 양 노드에 대해서, 해당 노드를 가기 위해 몇 개의 늑대/양 노드를 거쳐야 하는지 계산한다.
    let maxCount = 1
    const stack = [[-1, 1, startLambs, info]]

    while (stack.length > 0) {
        let [current, lambCount, tempLambs, tempInfo] = stack.pop()

        if (tempLambs.length < 1) {
            maxCount = Math.max(maxCount, lambCount)
            continue
        }

        let costs = tempLambs.map(idx => {
            let cost = -1
            let node = idx

            while (true) {
                node = parents[node]

                // 이미 방문한 노드인 경우
                if (tempInfo[node] === 0) {
                    maxCount = Math.max(maxCount, lambCount)
                    break
                }

                // 조상 노드 중 방문하지 않은 양 노드가 있는 경우 => 후보에서 제외
                if (tempInfo[node] === -1) {
                    return 'notCandidate'
                }
                cost += 1
            }
            return [cost, idx]
        }).filter(x => x !== 'notCandidate')

        // 새로 방문할 양 노드의 후보가 없는 경우
        if (costs.length < 1) {
            continue
        }

        lambCount += 1

        for (let [cost, idx] of costs) {
            // 현재 노드(idx)에 방문할 수 없는 경우
            if (current + cost > -2) {
                continue
            }

            let newCurrent = current + cost
            let lambs = [...tempLambs]
            let info = [...tempInfo]

            // 양 노드 목록(lambs)에서 현재 방문한 노드(idx)를 제거한다.
            for (let k = 0; k < lambs.length; k++) {
                if (lambs[k] === idx) {
                    lambs.splice(k, 1)
                    break
                }
            }

            // 새로 방문한 노드들에 방문 표시한다.
            while (info[idx] !== 0) {
                info[idx] = 0
                idx = parents[idx]
            }

            stack.push([newCurrent, lambCount, lambs, info])
        }
    }

    return maxCount
}
