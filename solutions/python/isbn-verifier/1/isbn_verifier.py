def is_valid(isbn):
    isbn_clean = isbn.replace('-', '')
    d = [10 if ch.upper() == 'X' and isbn_clean.endswith('X') else int(ch) if ch.isdigit() else False for ch in isbn_clean]
    if any(ch is False for ch in d) or len(d) != 10:
        return False
    w = list(range(10, 0, -1)) 
    test = sum(digit * weight for digit, weight in zip(d, w))
    return test % 11 == 0