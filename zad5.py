def list_contains(list: list, a: int) -> bool:
    if list.__contains__(a):
        return True
    else:
        return False


print(list_contains([1, 2, 3, 8], 7))
