function solution(id_list, report, k) {
    const N = id_list.length
    const reportedBy = {}
    const counts = {}

    for (let i = 0; i < N; i++) {
        reportedBy[id_list[i]] = []
        counts[id_list[i]] = 0
    }

    let reportSet = new Set(report)

    reportSet.forEach(current => {
        let [a, b] = current.split(' ')
        reportedBy[b].push(a)
    })

    for (let name in reportedBy) {
        let reporters = reportedBy[name]

        if (reporters.length >= k) {
            reporters.forEach(reporter => counts[reporter] += 1)
        }
    }
    const result = []

    for (let name in counts) {
        result.push(counts[name])
    }

    return result
}
