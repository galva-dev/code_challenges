def find_outlier(integers):
    parity = [('even' if num % 2 == 0 else 'odd') for num in integers]
    return integers[parity.index('odd' if parity.count('even') > 1 else 'even')]


print(find_outlier([2, 4, 6, 8, 3]))