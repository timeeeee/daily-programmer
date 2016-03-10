def decode_rec(total, power, n, base):
    max_len = min(len(str(base-1)), len(n))
    values = []
    for i in range(1, max_len+1):
        if len(n) > i:
            if not ((i > 1 and int(n[-i]) == 0) or int(n[-i:]) >= base):
                values += decode_rec(total+int(n[-i:])*base**power, power+1, n[:-i], base)
        elif len(n) == i and int(n) < base:
            values += [total + int(n)*base**power]
    return values

for n, base in [
        "101 2".split(),
        "101 16".split(),
        "120973 25".split(),
        "25190239128039083901283 100".split(),
        "251902391280395901283 2398".split()]:
    print decode_rec(0, 0, n, int(base))[:10]
