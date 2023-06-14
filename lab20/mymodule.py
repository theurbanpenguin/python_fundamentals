# mymodule.py

def basename(filepath):
    path_list = filepath.split('/')
    return path_list[-1]

def split_email(email):
    at = email.find('@')
    user = email[:at]
    domain = email[at + 1:]
    return {'user': user, 'domain': domain}
