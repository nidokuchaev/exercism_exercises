def recite(start, take=1):
    numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
    }
    
    lyrics = []

    k = start 
    for i in range(take):
        if k == 1:
            lyrics.append(f"One green bottle hanging on the wall,")
            lyrics.append(f"One green bottle hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            lyrics.append("There'll be no green bottles hanging on the wall.")
        else:
            lyrics.append(f"{numbers[k]} green bottles hanging on the wall,")
            lyrics.append(f"{numbers[k]} green bottles hanging on the wall,")
            lyrics.append("And if one green bottle should accidentally fall,")
            if k - 1 == 1: 
                lyrics.append(f"There'll be one green bottle hanging on the wall.")
            else:
                lyrics.append(f"There'll be {numbers[k - 1].lower()} green bottles hanging on the wall.")
        if i < take - 1:
            lyrics.append('')
        k -= 1
    return lyrics