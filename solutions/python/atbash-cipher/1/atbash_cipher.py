atbash = {chr(i): chr(219 - i) for i in range(97, 123)}

def encode(plain_text):
    encoded = [atbash[ch] if ch.isalpha() else ch for ch in plain_text.replace(' ', '').lower() if ch.isalpha() or ch.isdigit()]
    if len(encoded) < 5:
        return ''.join(encoded)
    else:
        return ''.join(v + ' ' if (i + 1) % 5 == 0 else v for i, v in enumerate(encoded)).strip()
def decode(ciphered_text):
    return ''.join([atbash[ch] if ch.isalpha() else ch for ch in ciphered_text.replace(' ', '').lower() if ch.isalpha() or ch.isdigit()])