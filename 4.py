def func(text):
    text = text.split()
    result_dict = dict.fromkeys(text, None)
    for i in result_dict:
        n = len(i)
        result_dict[i] = n
    print(result_dict)


loki = input("Enter a  text: ")
func(loki)
