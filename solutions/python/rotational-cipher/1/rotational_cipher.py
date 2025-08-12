def rotate(text, key):
    result = []
    for ch in text:
        if not ch.isalpha():
            result.append(ch)
            continue
            
        if ch.islower():
            i = ord(ch) - ord('a')
            new_pos = (i + key) % 26
            result.append(chr(new_pos + ord('a')))
        else:
            i = ord(ch) - ord('A')
            new_pos = (i + key) % 26
            result.append(chr(new_pos + ord('A')))
    return ''.join(result)