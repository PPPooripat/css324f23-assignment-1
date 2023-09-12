def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4, s[1] == 4

def successors(s):
    a, b, c = s

    t1 = 8 - a

    if t1 > 0 and b > 0:
        if b > t1:
            yield ((8, y-t1, c), t1)
        else:
            yield ((a + b, 0, c), b)

    if t1 > 0 and c > 0:
        if c > t1:
            yield ((8, y, c - t1), t1)
        else:
            yield ((a + c, b, 0), c)

    t2 = 5 - y

    if  t2 > 0 and x > 0:
        if a > t2:
            yield ((a - t2, 5, c), t2)
        else:
            yield ((0, b + a, c), a)

    if t2 > 0 and c > 0:
        if c > t2:
            yield ((a, 5, c - t2), t2)
        else:
            yield ((a, b + c, 0), c)

    t3 = 3 - c

    if t3 > 0 and b > 0:
        if b > t3:
            yield ((a, b - t3, 3), t3)
        else:
            yield ((0, b, c + a), a)

    if t3 > 0 and b > 0:
        if b > t3:
            yield ((a, b - t3, 3), t3)
        else:
            yield ((x, 0, c + b),b)
                   
