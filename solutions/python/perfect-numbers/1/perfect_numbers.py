def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    total = sum(factors)

    if total == number:
        return 'perfect'

    if total <= number:
        return 'deficient'

    if total >= number:
        return 'abundant'

    