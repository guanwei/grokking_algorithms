def sum(lst):
    if lst == []:
        return 0
    return lst[0] + sum(lst[1:])