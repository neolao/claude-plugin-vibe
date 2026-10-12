"""Invoice totals, called from the billing job."""


def calc(l, r):
    t = 0
    for x in l:
        t += x * (1 + r)
    return t
