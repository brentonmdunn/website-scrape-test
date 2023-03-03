import json

my_list = [
        {"hobby1": "swimming"},
        {"hobby2": "snow"}
    ]

my_list.append({"hobby3": "water"})

dictionary = {
    "hobby4": "climbing"
}

json_object = json.dumps(dictionary)

print(json_object)

my_list.append(dictionary)
# str(my_list[3]).replace("\"", "NO")

dictionary = {
    "first_name": "Brenton",
    "last_name": "Dunn",
    "birthday": "12/30/2003",
    "hobbies": my_list
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)