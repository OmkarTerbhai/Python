# Lists in Python

my_list = ["Demo", "Hello", "Fun", "Gun", "Mun"];

print(len(my_list));

print("Fun" in my_list);

my_list.append("1");
print("After using str.append(): ", my_list);

my_list += ["2"];
print("After using += ", my_list);

my_list.insert(1, "Omkar");
print(my_list);

my_list[2:5] = ["Hello123"];
print(my_list);

