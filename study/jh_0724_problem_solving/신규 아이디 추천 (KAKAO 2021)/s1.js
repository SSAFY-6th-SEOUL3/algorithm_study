function solution(new_id) {
      // 1단계
      new_id = new_id.toLowerCase()

      // 2단계
      let result = ""

      for (let char of new_id) {
          if ('abcdefghijklmnopqrstuvwxyz0123456789-_.'.includes(char)) {
              result += char
          }
      }

      // 3단계
      result = [...result]

      idx = 0

      while (idx < result.length) {
          if (result[idx] === '.') {
              idx += 1
              while (idx < result.length && result[idx] === '.') {
                  result[idx] = ''
                  idx += 1
              }
          } else {
              idx += 1
          }
      }

      result = result.join('')

      // 4단계 + 5단계
      start_idx = 0
      end_idx = result.length - 1

      while (start_idx <= end_idx && result[start_idx] == '.') {
          start_idx += 1
      }

      if (start_idx > end_idx) {
          result = "a"
      } else {
          while (result[end_idx] == '.') {
              end_idx -= 1
          }

          result = result.substring(start_idx, end_idx + 1)
      }

      // 6단계 + 7단계
      if (result.length > 15) {
          result = result.substring(0, 15)

          while (result[result.length - 1] === '.') {
              result = result.substring(0, result.length - 1)
          }
      } else if (result.length < 3) {
          for (let c = 0; c < 4 - result.length; c++) {
              result += result[result.length - 1]
          }
      }

      return result
}
