# Dictionaries in Python

my_dict = {
    "key1": "value1",
    "key2": "value2"
};

print(my_dict);

my_dict2 = {
    "key3": "value3",
    "key4": "value4"
};

print(my_dict2);

my_dict3 = {
    "dict 1" : my_dict,
    "dict 2" : my_dict2
};

print(my_dict3);

# Dictionary Methods

my_dict.update({"key n": "value n"});
print(my_dict);

print(my_dict3.get("dict 2"));