hero_list: list[str] = [
    "deku",
    "red-riot",
    "lemillion",
    "suneater",
    "uravity",
    "all-might",
]

hero_id = [1211, 1401, 5058, 4078, 9636, 7812]



print(dict(zip(hero_list,hero_id)))


print("\n")
print(set(zip(hero_list,hero_id)))
print("\n")
print(list(zip(hero_list,hero_id)))