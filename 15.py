import random

password = ""
input_length = int(input("Enter length of the password: "))
for i in range(input_length):
    password += str(random.randint(0, 9))
print(password)
