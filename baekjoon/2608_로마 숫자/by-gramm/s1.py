
to_roman = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM'],
]

to_num = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

to_num2 = {
    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
}


def roman_to_num(roman):
    """
    로마 숫자를 아라비아 숫자로 변환한다.
    """
    num = 0

    for r, n in to_num2.items():
        if r in roman:
            num += n
            roman = roman.replace(r, "")

    for r, n in to_num.items():
        num += (n * roman.count(r))

    return num


def num_to_roman(num):
    """
    아라비아 숫자를 로마 숫자로 변환한다.
    """
    roman = ""
    i = 0

    while num:
        num, rest = divmod(num, 10)
        roman = to_roman[i][rest] + roman
        i += 1

    return roman


roman1 = input().strip()
roman2 = input().strip()

total = roman_to_num(roman1) + roman_to_num(roman2)
print(f"{total}\n{num_to_roman(total)}")
