def distance(strand_a, strand_b):
    k = 0 
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for i, l in enumerate(strand_a):
        for o, d in enumerate(strand_b):
            if i == o and l != d:
                k += 1
    return k