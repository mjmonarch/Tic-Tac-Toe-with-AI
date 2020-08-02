def last_indexof_max(numbers):
    index_max = 0
    if not numbers:
        return -1
    if len(numbers) == 1:
        return 0
    for index in range(1, len(numbers)):
        if numbers[index] >= numbers[index_max]:
            index_max = index
    return index_max
