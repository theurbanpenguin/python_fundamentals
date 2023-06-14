from sys import argv
from mymodule import basename

script_name = basename(argv[0])
names = []

try:
    argv[1].isalnum()
    for n in sys.argv[1:]:
        names.append(n)
except IndexError:
    names.append(input(f'The script {script_name} requires a name, enter it now: '))
finally:
    for n in names:
        print(n)
