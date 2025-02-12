# hero_list: list[str] = [
#     "deku",
#     "red-riot",
#     "lemillion",
#     "suneater",
#     "uravity",
#     "all-might",
# ]


# print([f"my favourite hero is {hero}" for hero in hero_list])


##-----------------comprehension + conditions ------------------------##

# hero_list: list[str] = [
#     "deku",
#     "red-riot",
#     "lemillion",
#     "suneater",
#     "uravity",
#     "all-might",
# ]

# top_hero =[
#     "all-might",
#     "eraser-head",
#     "lemillion"

# ]

# x =  [
#         hero.title()
#         for hero in hero_list
#         if(hero.lower() in [hero.lower() for hero in top_hero])

#     ]
# print(
#    x
# )


##-----------------dictonary comprehension------------------------##
hero_list: list[str] = [
    "deku",
    "red-riot",
    "lemillion",
    "suneater",
    "uravity",
    "all-might",
]

hero_id = [1211, 1401, 5058, 4078, 9636, 7812]

x = {hero_list[i]: hero_id[i] for i in range(len(hero_id))}

print(x)
