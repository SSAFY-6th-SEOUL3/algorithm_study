const getParkingFee = (fees, parkingTime) => {
    const [basicTime, basicFee, unitTime, unitFee] = fees

    if (parkingTime <= basicTime) {
        return basicFee
    }

    return basicFee + Math.ceil((parkingTime - basicTime) / unitTime) * unitFee
}


function solution(fees, records) {
    inRecords = {}
    result = {}

    // 각 기록을 순회하면서 차량들이 주차장에 머문 시간을 저장한다.
    records.forEach(record => {
        let [time, carNum, info] = record.split(" ")
        let [hour, minute] = time.split(":")
        time = parseInt(hour * 60) + parseInt(minute)

        if (info[0] === 'I') {
            inRecords[carNum] = time
        } else {
            let parkingTime = time - inRecords[carNum]
            result[carNum] = (carNum in result) ? result[carNum] + parkingTime : parkingTime
            delete inRecords[carNum]
        }
    })

    // 출차된 내역이 없는 차량들의 주차 시간을 저장한다.
    for (let carNum in inRecords) {
        let parkingTime = 1439 - inRecords[carNum]
        result[carNum] = (carNum in result) ? result[carNum] + parkingTime : parkingTime
    }

    const resultArr = []

    // 차량번호별로 주차요금을 계산한다.
    for (let carNum in result) {
        resultArr.push([parseInt(carNum), getParkingFee(fees, result[carNum])])
    }

    // 차량 번호가 작은 순으로 정렬한 뒤, 주차 요금을 배열에 담아 리턴한다.
    resultArr.sort((a, b) => a[0] - b[0])
    return resultArr.map(x => x[1])
}
