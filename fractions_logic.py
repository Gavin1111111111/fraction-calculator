def simplify(num, denom):
    i = 2
    while i <= abs(num) and i <= abs(denom):
        if (num % i == 0 and denom % i == 0):
            num //= i
            denom //= i
            i = 2
        else:
            i += 1
    return num, denom

def mult_fractions(num1, denom1, num2, denom2):
    if denom1 == 0 or denom2 == 0:
        return None
    final_num = num1 * num2
    final_denom = denom1 * denom2
    return simplify(final_num, final_denom)


def div_fractions(num1, denom1, num2, denom2):
    if denom1 == 0 or denom2 == 0:
        return None
    final_num = num1 * denom2
    final_denom = denom1 * num2
    return simplify(final_num, final_denom)

def minus_fractions(num1, denom1, num2, denom2):
    if denom1 == 0 or denom2 == 0:
        return None

    if denom1 == denom2:
        return simplify(num1 - num2, denom1)

    final_denom = denom1 * denom2
    final_num = num1 * denom2 - num2 * denom1
    return simplify(final_num, final_denom)


def add_fractions(num1, denom1, num2, denom2):
    if denom1 == 0 or denom2 == 0:
        return None

    if denom1 == denom2:
        return simplify(num1 + num2, denom1)

    final_denom = denom1 * denom2
    final_num = num1 * denom2 + num2 * denom1
    return simplify(final_num, final_denom)
