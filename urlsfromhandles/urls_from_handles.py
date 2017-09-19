# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2"]


def urls_from_handles(names_list):
    greenfox_string = "https://github.com/greenfox-academy/"
    for i in (range(len(names_list))):
        names_list[i] = greenfox_string + names_list[i]
    return names_list


print(urls_from_handles(names))