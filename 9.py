given_str = input("enter a string: ")
new_string = ""
n = 0
for i in given_str:
    if i.isalpha():
        n += 1
        new_string += i + str(n)
print(new_string)
