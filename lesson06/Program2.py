# Sets in Python

my_set = {10, 20, 30, 40, 50, 40};

my_set2 = my_set.union({60, 50, 30});

print(my_set2);

set3 = my_set.intersection({30, 40, 50, 60});
print(set3);

set4 = my_set.difference({30, 40, 50, 60});
print(set4);
