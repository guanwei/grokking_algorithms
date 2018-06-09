def count(lst):
    if lst == []:
        return 0
    return 1 + count(lst[1:])