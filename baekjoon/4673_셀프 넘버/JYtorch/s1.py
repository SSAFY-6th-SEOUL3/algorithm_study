numbers = [0] * 10001

for i in range(1, 10001):
    number = 0
    while number <= 10000:

        number = str(i)
        numsum = 0

        for n in number:
            numsum += int(n)

        number = int(number) + numsum
        if number > 10000: break
        numbers[number] += 1
        i = number

for i in range(1, len(numbers)):
    if numbers[i] == 0:
        print(i)
