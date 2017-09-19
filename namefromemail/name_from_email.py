# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter



def name_from_email(email_address):
    first_name_string= ""
    last_name_string=""
    full_name = ""
    flag = False
    for i in range(len(email_address)):
        if email_address[i] != "@" and flag == False:
            full_name += email_address[i]
        else:
            flag = True
    full_name_flag = False
    for i in range(len(full_name)):
        if full_name[i] != "@" and flag == False:
            last_name_string += full_name[i]
        else:
            last_name_string += full_name[i]
            

    return (last_name_string + " " + first_name_string)


print(name_from_email("elek.viz@exam.com"))