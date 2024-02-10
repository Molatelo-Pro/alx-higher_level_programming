#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
my_list = [10, 20, 30, 40, 50]
index = 2
result = element_at(my_list, index)
print(result)
