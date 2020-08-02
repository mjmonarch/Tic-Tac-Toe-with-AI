def startswith_capital_counter(names):
    res = 0
    for name in names:
        if name.istitle():
            res += 1
    return res
