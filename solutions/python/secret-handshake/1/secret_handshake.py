def commands(binary_str):
    decode = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump',
        4: 'reverse'
    }

    ans = []
    
    for i, d in enumerate(binary_str[::-1]): # 00001
        if d == '1':
            if i == 4:
                ans.reverse()
            else:
                ans.append(decode[i])
    return ans