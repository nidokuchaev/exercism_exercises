def answer(question):

    operations = {
        'plus': lambda x, y: x + y,
        'minus': lambda x, y: x - y,
        'divided': lambda x, y: x // y,
        'multiplied': lambda x, y: x * y,
    }

    words = [w.strip('?') for w in question.split()]
    
    numbers = [int(n) for n in words if n.isdigit() or n.startswith('-')]
    ops = [op for op in words if op in operations]

    for i in range(len(words) - 1):
        try:
            current_num = int(words[i])
            next_num = int(words[i + 1])
        except ValueError:
            continue
        if current_num in numbers and next_num in numbers:
            raise ValueError('syntax error')

    if len(numbers) == 0 or len(ops) == len(numbers):
        raise ValueError('syntax error')

    try:
        int(words[-1])
    except ValueError:
        raise ValueError('unknown operation')

    result = numbers[0]
    
    for i, op in enumerate(ops):
        if i + 1 < len(numbers):
            func = operations[op]
            result = func(result, numbers[i + 1])
    return result
            