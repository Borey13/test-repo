my_dict = {"name1": "id1",
           "name2": "id2",
           "name3": "id3"
           }

list_keys = list(my_dict.keys())
list_values = list(my_dict.values())
new_dict = {}
index_keys = 0
for value in list_values:
    new_dict[value] = list_keys[index_keys]
    index_keys += 1

print(new_dict)
