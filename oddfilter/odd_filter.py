# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

odd_filter = [1, 2, 3, 4, 5]  # should print [1, 3, 5]


def odd_number_filter_func(number_list):
    filtered_list = []
    for element in number_list:
        if element % 2 != 0:
            filtered_list.append(element)
    return filtered_list


print(odd_number_filter_func(odd_filter))
