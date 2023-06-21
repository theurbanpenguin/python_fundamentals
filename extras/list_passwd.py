passwd_file = "/etc/passwd"
users_dict = {}

with open(passwd_file, 'r') as file:
    for line in file:
        fields = line.strip().split(':')
        username = fields[0]
        uid = fields[2]
        gid = fields[3]
        full_name = fields[4]
        home_dir = fields[5]
        shell = fields[6]

        users_dict[username] = {
            'uid': uid,
            'gid': gid,
            'full_name': full_name,
            'home_dir': home_dir,
            'shell': shell
        }

# Printing the dictionary of users
for username, details in users_dict.items():
    print(f"Username: {username}")
    print(f"User ID: {details['uid']}")
    print(f"Group ID: {details['gid']}")
    print(f"Full Name: {details['full_name']}")
    print(f"Home Directory: {details['home_dir']}")
    print(f"Shell: {details['shell']}")
    print()