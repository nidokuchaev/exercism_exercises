def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    num = 0
    
    for i, d in enumerate(reversed(digits)):
        num += d * (input_base ** i)

    if num == 0:
        return [0]

    encoded_digits = []

    while num > 0:
        remainder = num % output_base
        encoded_digits.append(remainder)
        num = num // output_base
    return encoded_digits[::-1]