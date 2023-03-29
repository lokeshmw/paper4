def func(given_list):
    new_list = []
    for i in given_list:
        if i == i[::-1]:
            new_list.append(i)
    return new_list


kil = [x for x in input("enter: ").split()]
print(func(kil))
