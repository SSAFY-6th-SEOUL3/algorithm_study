/**
 * 10진수 수 num을 k진수로 나타낸 문자열을 리턴한다.
 * (3 <= k <= 10)
 */
const toKth = (num, k) => {
    let result = ""

    while (num > 0) {
        let rest = num % k
        result = rest + result
        num = (num - rest) / k
    }

    return result
}


/**
 * 인자로 들어온 수(num)가 소수면 true, 아니면 false를 리턴한다.
 */
const isPrime = num => {
    if (num === 1) return false
    if (num === 2) return true
    if (num % 2 == 0) return false

    for (let i = 3; i < parseInt(Math.sqrt(num) + 1); i += 2) {
        if (num % i == 0)  return false
    }

    return true
}


function solution(n, k) {
    const numbers = toKth(n, k).split('0')
    let count = 0

    numbers.forEach(num => {
        if (num !== "" && isPrime(parseInt(num))) count++
    })

    return count
}