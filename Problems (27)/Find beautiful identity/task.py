def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if str(id(i))[-3:] == '888':
            return i
    return None
