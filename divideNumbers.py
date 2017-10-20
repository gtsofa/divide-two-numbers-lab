def divideTwoNumbers(numerator, denominator):
    if denominator == 0:
        raise ValueError
    else:
        result = numerator/denominator
        return result
