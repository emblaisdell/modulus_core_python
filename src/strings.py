from modulus import calculation

@calculation(["string","string"])
def replaceLast(fmt, a):
    # https://stackoverflow.com/questions/2556108/rreplace-how-to-replace-the-last-occurrence-of-an-expression-in-a-string
    return a.join(fmt.rsplit("%s", 1))

@calculation(["integer"])
def intToString(a):
    return str(a)

@calculation(["string","string"])
def concatenate(a,b):
    print(a)
    print(b)
    return a+b
