def average_mark(*marks):
    total = 0
    for mark in marks:
        total += mark
    return round(total / len(marks), 1)
