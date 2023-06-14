# mymodule.py

def basename(filepath):
    path_list = filepath.split('/')
    return path_list[-1]

def split_email(email):
    at = email.find('@')
    user = email[:at]
    domain = email[at + 1:]
    return {'user': user, 'domain': domain}

def f_to_c(fahrenheit):
    return (fahrenheit - 32) / 1.8

def prompt_for_int(message, value):
    count = 1

    while not value.isdigit():
        if count < 2:
            value = input(message)
            if value.isdigit():
                break
        elif count > 3:
            print('Unable to convert user input')
            exit(1)
        else:
            value = input("Please enter an integer, i.e. 1, 77, 104, etc: ")
            if value.isdigit():
                break
        count = count + 1

    return int(value)

