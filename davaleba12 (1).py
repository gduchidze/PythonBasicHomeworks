#1
# def remove_dup(input):
#     uniq_set = set()
#     res_dictionary = {}
#
#     for key, value in input.items():
#         if value not in uniq_set:
#             uniq_set.add(value)
#             res_dictionary[key] = value
#
#     return res_dictionary
#
# dict = {'a': 11, 'b': 33, 'c': 111, 'd': 33, 'e': 222, 'f': 11}
# print(remove_dup(dict))

#2

# def empty_dict(my_dict):
#     return not bool(my_dict)
#
# x = {}
# y = {'1': '2'}
#
# if empty_dict(x):
#     print("ცარიელია")
# else:
#     print("არ არის ცარიელი")
#
# if empty_dict(y):
#     print(" ცარიელია ")
# else:
#     print("არ არის ცარიელი")

#3
# . დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი,
# უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს
# ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}

def count_dict(input):
    chount_dict = {}

    for char in input:
        if char in chount_dict:
            chount_dict[char] += 1
        else:
            chount_dict[char] = 1

    return chount_dict

x = 'racoon'
print(count_dict(x))
