test = []
result = []

with open("file_1", "r") as f:
    data = f.readlines()
    for i in data:
        test.append(i[:5])


with open("file_2", "r") as f:
    data = f.readlines()
    for i in data:
        result.append(i[:4])

merge = zip(test, result)
print(dict(merge))
