student_det = [
    {"name": "Dev", "id": 0, "age": 21},
    {"name": "arsh", "id": 1, "age": 22},
    {"name": "gagan", "id": 2, "age": 22},
]

for item in student_det:
    for naam, identity in item.items():
        print(naam, str(identity))

    print("----------------------------------------")