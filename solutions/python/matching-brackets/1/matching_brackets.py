def is_paired(input_string):
    brackets = {'[':']', '{':'}', '(':')'}
    buffer = []
    for ch in input_string:
        if ch in brackets:
            buffer.append(ch)
        elif ch in brackets.values():
            if not buffer:
                return False
            last_open = buffer.pop()
            if brackets[last_open] != ch:
                return False
    return not buffer