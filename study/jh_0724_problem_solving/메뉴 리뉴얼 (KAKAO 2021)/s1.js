const getCombinations = (arr, r) => {
    let result = []
    
    if (r === 1) {
        for (let element of arr) {
            result.unshift(element)
        }
        return result
    }
    
    for (let i = 0; i < arr.length - r + 1; i++) {
        let rest = getCombinations(arr.slice(i + 1), r - 1)
        
        for (let comb of rest) {
            result.push(arr[i] + comb)
        }     
    }
    
    return result
}


function solution(orders, course) {
    const result = []
    
    // 각 course의 개수 num에 대하여
    for (let num of course) {
        // num개짜리 메뉴 조합의 주문 횟수를 모두 구한 뒤 
        const orderCount = {}
        
        for (let order of orders) {
            order = [...order].sort()

            let combs = getCombinations(order, num)
            
            for (let comb of combs) {
                if (comb in orderCount) {
                    orderCount[comb] += 1
                } else {
                    orderCount[comb] = 1
                }
            }
        }
        
        // 주문 횟수가 가장 많은 메뉴 조합들을 result에 저장한다.
        let maxCount = 0
        
        for (let count of Object.values(orderCount)) {
            maxCount = Math.max(count, maxCount)
        }
        
        if (maxCount < 2) continue
        
        for (let [menuSet, count] of Object.entries(orderCount)) {
            if (count === maxCount) {
                result.push(menuSet)
            }
        }
    }

    result.sort()
    return result
}
