import sys
sys.stdin = open('input.txt')

"""
500 50 1 1 1
1000 100 1000 10 50
    1100
        1900
             1910
                 1940    
"""
def roma_to_arab(string):
    N = len(string)
    num_set = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    curr = string[0]
    total = num_set[curr]

    for i in range(1, N):
        prev, curr = curr, string[i]
        if num_set[prev] >= num_set[curr]:
            total += num_set[curr]
        else:
            total += num_set[curr] - num_set[prev] * 2

    return total


def arab_to_roma(number):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roma_list = roms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(num_list)):
        start = number // num_list[i]
        result += roma_list[i] * start
        number -= num_list[i] * start
    # for i in range(len(roma_num_list)):
    #     roma_num = roma_num_list[i]
    #     while number >= roma_num:
    #         result += rom_set[roma_num]
    #         number -= roma_num

    return result


roma_num1 = input()
roma_num2 = input()

res = roma_to_arab(roma_num1) + roma_to_arab(roma_num2)
print(res)
print(arab_to_roma(res))
