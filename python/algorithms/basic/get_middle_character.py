def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s) / 2) - 1 : int(len(s) / 2 + 1)]
    else:
        return s[int(len(s) / 2)]


print(get_middle("a"))
