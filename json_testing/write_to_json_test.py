import json

dictionary = {
    "first_name": "Brenton",
    "last_name": "Dunn",
    "birthday": "12/30/2003",
    "hobbies": [
        {"hobby1": "swimming"},
        {"hobby2": "snow"}
    ]
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)