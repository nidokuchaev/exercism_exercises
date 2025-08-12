def label(colors):
    translation = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    ans = [translation[n] for n in colors if n in translation][:3]

    conversion = int(''.join(str(x) for i, x in enumerate(ans) if i != 2) + '0' * ans[2])

    metric_prefixes = {
        'ohms': 1,
        'kiloohms': 10**3,
        'megaohms': 10**6,
        'gigaohms': 10**9
    }

    for prefix, val in sorted(metric_prefixes.items(), key=lambda x: x[1], reverse=True):
        if conversion >= val:
            return f'{conversion // val} {prefix}'
    return f'{conversion} ohms'