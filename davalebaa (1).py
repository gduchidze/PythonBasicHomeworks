#1
def unique_list(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

x = [1, 2, 2, 3, 4, 4, 5]
print(unique_list(x))

#2

def immutable_set(input_list):
    x = frozenset(input_list)
    return x

y = [1, 2, 2, 3, 4, 4, 5]
print(immutable_set(y))

#3

def set_to_tuple(set1, set2):
    cset = set1.union(set2)
    x = tuple(cset)
    return x

a = {1, 2, 3}
b = {3, 4, 5}
print(set_to_tuple(a, b))

