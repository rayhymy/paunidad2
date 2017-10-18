def presion(l: float, m: float, t: float) -> float:
    p = (l ** -1) * m * (t ** -2)
    return p


def caudal(l: float, t: float) -> float:
    c = (l ** 3) * (t ** -1)
    return c
