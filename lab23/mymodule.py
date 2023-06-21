def basename(filepath):
    path_list = filepath.split('/')
    return path_list[-1]

def split_email(email):
    at = email.find('@')
    user = email[:at]
    domain = email[at + 1:]
    return { 'user':user, 'domain':domain}

def f_to_c(fahrenheit):
    return (fahrenheit - 32) / 1.8

def c_to_f(centigrade):
    return (centigrade * 9/5) + 32

def prompt_for_int(message,value):
    count = 1
    while not value.isdigit():
        if count < 2:
            value = input(message)
            if value.isdigit():
                break
        elif count > 3:
            print('Unable to help you   ')
            exit(1)
        else:
            value = input('Unable to convert your number make sure it is an integer, 1 3, 6 etc: ')
            if value.isdigit():
                break
        count = count + 1
    return int(value)

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

