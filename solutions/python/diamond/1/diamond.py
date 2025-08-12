alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def rows(letter):
    ans = []
    i = alphabet.index(letter)
    for j in range(i + 1):
        if j == 0:
            row = ' ' * (i - j) + alphabet[j] + ' ' * (i - j)
        else:
            row = ' ' * (i - j) + alphabet[j] + ' ' * (2 * j - 1) + alphabet[j] + ' ' * (i - j)
        ans.append(row)
    return ans + ans[-2::-1]