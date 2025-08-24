def egg_count(display_value):
    n = display_value
    remainder = n
    k = 0
    ans = 0
    while 2 ** k <= n:
        k +=1

    for i in range(k, -1, -1):
        largest_power = 2 ** i
        if largest_power <= remainder:
            ans += 1
            remainder -= largest_power

    return ans