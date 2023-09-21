def list_element_checker(x):
    a = x

    if a[0] == a[-1]:
        return True

    else:
        return False


x = [10, 20, 30, 40, 10]
print(list_element_checker(x))

y = [75, 65, 35, 75, 30]
print(list_element_checker(y))
