import json


def func():
    a = open("loki.json")
    data = json.load(a)
    for i in data['my_details']:
        print(i)
    a.close()


func()
