def find_anagrams(word, candidates):

    ans = []

    for w in candidates:
        if all(l in word.lower() and len(w) == len(word) and w.lower() != word.lower() and w.lower().count(l) <= word.lower().count(l) for l in w.lower()):
            ans.append(w)
    return ans