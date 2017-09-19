# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter



def name_from_email(email_address):
    last_name_string =""
    first_name_string =""
    flag_first_point = False
    flag_second_point = False
    for i in range(len(email_address)):
       if flag_first_point == False and flag_second_point == False:
            if email_address[i] != "." and flag_first_point == False and flag_second_point == False:
               first_name_string += email_address[i]
            elif email_address[i] != "@" and flag_first_point == True and flag_second_point == False:
                last_name_string += email_address[i]
            elif email_address[i] == ".":
                flag_first_point == True
            elif email_address[i] == "@":
                break
                

    full_name = first_name_string + " " + last_name_string

    return (full_name)


print(name_from_email("elek.viz@exam.com"))