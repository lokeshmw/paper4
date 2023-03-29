import json
a = open("employee_data.json")
data = json.load(a)
b = data["employee_data"][0]["priya"]["Location"]
print(b)
a.close()
