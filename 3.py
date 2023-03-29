given_list = [int(x) for x in input("enter a list: ").split()]
even_list = []
odd_list = []
for i in given_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

dict_ = {"even": even_list, "odd": odd_list}
print(dict_)
