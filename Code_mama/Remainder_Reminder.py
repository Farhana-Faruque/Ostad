def modulo():
    a, b = map(int, input().split())
    if b == 0:
        return None
    c = a % b 
    return c