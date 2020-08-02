def range_sum(numbers, start, end):
    res = 0
    for number in numbers:
        if start <= number <= end:
            res += number
    return res


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))