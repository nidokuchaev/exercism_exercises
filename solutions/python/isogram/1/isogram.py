def is_isogram(string):
    seen = set()
    for letter in string.lower():
        if letter in ('-', ' '):
            continue
        if letter in seen:
            return False
        seen.add(letter)
    return True