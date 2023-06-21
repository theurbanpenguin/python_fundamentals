import sys
import mymodule

script_name = basename(sys.argv[0])
names = []

try:
    sys.argv[1].isalnum()
    for n in sys.argv[1:]:
        names.append(n)
except IndexError:
    names.append(input(f'The script {script_name} requires a name, enter it now: '))
finally:
    for n in names:
        print(n)
