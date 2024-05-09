def array_diff(a, b):
    return list(filter(lambda x: x not in b, a))


print(array_diff([1, 2, 3, 4], [1, 2]))
