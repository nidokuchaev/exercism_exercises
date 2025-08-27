def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for l in lists for item in l]


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    return len(list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc


def foldr(function, list, initial):
    acc = initial
    for el in reversed(list):
        acc = function(acc, el)
    return acc


def reverse(list):
    return list[::-1]
