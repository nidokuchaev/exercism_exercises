def flatten(iterable):
    clean = []
    for i in iterable:
        if isinstance(i, list):
            clean.extend(flatten(i))
        elif i is not None:
            clean.append(i)
    return clean