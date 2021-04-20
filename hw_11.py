# Task 2
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
result_set = set.intersection(set1, set2, set3)
print(result_set)

# Task 3
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
result_set = set.difference(set1, set2, set3)
print(result_set)

# Task 4
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
result_set = set.union(set1, set2, set3)
print(result_set)

# Task 5
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
result_set = sampleSet.union(sampleList)
print(result_set)

# Task 6
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result_set = set1.intersection(set2)
print(result_set)

# Task 7
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
total = set1.union(set2)
print(total)

# Task 8
set1 = {10, 20, 30}
set2 = {20, 40, 50}
total = set1.difference(set2)
print(total)

# Task 9
set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print(set1)

# Task 11
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
total = set1.intersection(set2)
print(total)

# Task 12
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
total = set1.union(set2)
print(total)

# Task 13
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
total = set1.difference(set2)
print(total)
set1.discard(10)
set1.discard(20)
print(set1)

# Task 14
lst = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3, 9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
clean_list = []
for elem in lst:
    types = [(type(sym)).__name__ for sym in elem if (type(sym)).__name__]
    single_types = []
    [single_types.append(i_types) for i_types in types if i_types not in single_types]
    types_count = [types.count(element_type) for element_type in single_types]
    max_types_count = max(types_count)
    index_max = types_count.index(max(types_count))
    main_type = single_types[index_max]
    separated_list = [element for element in elem if type(element).__name__ == main_type]
    clean_list.extend(separated_list)
res_int_lst = [k for k in clean_list if type(k) == int]
res_float_lst = [k for k in clean_list if type(k) == float]
res_str_lst = [k for k in clean_list if type(k) == str]
print("clean list copy", clean_list)
print("list with integer type of numbers", res_int_lst)
print("list with float type of numbers", res_float_lst)
print("list with string type of numbers", res_str_lst)
