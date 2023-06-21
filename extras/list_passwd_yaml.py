import yaml

passwd_file = "/etc/passwd"
users_list = []

with open(passwd_file, 'r') as file:
    for line in file:
        fields = line.strip().split(':')
        username = fields[0]
        uid = fields[2]
        gid = fields[3]
        full_name = fields[4]
        home_dir = fields[5]
        shell = fields[6]

        user_data = {
            'username': username,
            'uid': uid,
            'gid': gid,
            'full_name': full_name,
            'home_dir': home_dir,
            'shell': shell
        }

        users_list.append({username: user_data})

# Convert the list to YAML format
yaml_data = yaml.dump(users_list)

# Print the YAML data
print(yaml_data)