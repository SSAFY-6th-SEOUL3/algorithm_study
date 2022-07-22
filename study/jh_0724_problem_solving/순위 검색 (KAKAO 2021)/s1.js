const binarySearch = (arr, target) => {
    let start = 0
    let end = arr.length - 1
    let mid = 0
    
    while (start <= end) {
        mid = parseInt((start + end) / 2)
        
        if (arr[mid] < target) {
            start = mid + 1
        } else if (arr[mid] > target) {
            end = mid - 1
        } else {
            while (mid < arr.length - 1 && arr[mid - 1] == target) {
                mid--
            }
            return mid
        }
    }
    
    return start
}


const getAbbr = (arr) => {
    let abbr = ""
    
    for (let element of arr) {
        abbr += element[0]
    }
    
    return abbr
}


function solution(info, query) {
    // 1. 각 지원자의 정보를 저장한다.
    const infoDict = {}
    
    info.forEach(subInfo => {
        subInfo = subInfo.split(' ')
        let point = parseInt(subInfo.pop())
        let abbr = getAbbr(subInfo)
        
        if (abbr in infoDict) {
            infoDict[abbr].push(point)
        } else {
            infoDict[abbr] = [point]
        }       
    })
    
    for (let abbr in infoDict) {
        infoDict[abbr].sort((a, b) => a - b)
    }

    // 2. 각 쿼리를 만족하는 지원자의 수를 구한다.
    const counts = []
    
    query.forEach(curr => {
        curr = curr.split(' and ')
        let foodAndPoint = curr.pop().split(' ')
        
        curr.push(foodAndPoint[0])
        let currAbbr = getAbbr(curr)
        let currPoint = parseInt(foodAndPoint[1])
        
        let count = 0
        
        for (let abbr in infoDict) {
            let flag = true
            
            for (let i = 0; i < 4; i++) {
                if (currAbbr[i] === '-')  continue
                
                if (abbr[i] !== currAbbr[i]) {
                    flag = false
                    break
                }
            }
            
            if (flag) {
                count += (infoDict[abbr].length - binarySearch(infoDict[abbr], currPoint))
            }
        }
        
        counts.push(count)
    })

    return counts
}
