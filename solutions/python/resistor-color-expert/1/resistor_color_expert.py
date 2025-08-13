def resistor_label(colors):

    colors_to_value = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }

    tolerances = {
        'grey': 0.05,
        'violet': 0.1,
        'blue': 0.25,
        'green': 0.5,
        'brown': 1,
        'red': 2,
        'gold': 5,
        'silver': 10
    }

    metric_prefixes = {
        'ohms': 1,
        'kiloohms': 10**3,
        'megaohms': 10**6,
        'gigaohms': 10**9
    }

    if len(colors) == 1:
        return f'{colors_to_value[colors[0]]} ohms'
    
    convert = [colors_to_value[n] for n in colors if n in colors_to_value]
    add_zeros = int(''.join(str(v) for v in convert[:-2]) + '0' * convert[-2])
    resistance = [tolerances[r] for r in colors if r in tolerances][-1]

    for prefix, v in sorted(metric_prefixes.items(), key=lambda x: x[1], reverse=True):
        if add_zeros >= v:
            add_prefix = add_zeros / v
            if add_prefix % 1 == 0:
                add_prefix = int(add_prefix)
                return f'{add_prefix} {prefix} ±{resistance}%'
            else:
                return f'{add_prefix} {prefix} ±{resistance}%'
    return f'{add_zeros} ohms ±{resistance}%'