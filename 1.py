given_list = [2, 3, -5, -7, 9, 4, 6, -1, -8, 0]
for i in range(len(given_list)):
    for j in range(0, len(given_list)-1):
        if given_list[j] > given_list[j+1]:
            given_list[j], given_list[j+1] = given_list[j+1], given_list[j]
print(given_list)
