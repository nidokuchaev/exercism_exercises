def translate(text):
    vowel = ('a', 'e', 'i', 'o', 'u')
    
    consonant = (
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    )

    res = []

    for word in text.split():
        buffer = []
        if word.startswith(vowel) or word.startswith('xr') or word.startswith('yt'):
            res.append(word + 'ay')
            break
        if word.startswith(consonant):
            for i, cons in enumerate(word):
                if i + 1 < len(word):
                    if cons in consonant:
                        buffer.append(cons)
                    if cons == 'q' and word[i + 1] == 'u':
                        buffer.append('u')
                    if cons in consonant and word[i + 1] == 'y':
                        res.append(word[len(buffer):] + ''.join(buffer) + 'ay')
                        break
                    if word[i + 1] in vowel:
                        res.append(word[len(buffer):] + ''.join(buffer) + 'ay')
                        break
    return ' '.join(res)