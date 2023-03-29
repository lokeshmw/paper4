given_tuple = "user1"
result = (given_tuple,) + ('password1',)
print(result)
n = 2007

try:
    given_tuple + n

except TypeError:
    print("Error: cannot concatenate string and Number")
