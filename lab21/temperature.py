import sys
import mymodule
file = mymodule.basename(sys.argv[0])
message = file + ' : Enter a temp: '
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
    except ValueError:
        temp = mymodule.prompt_for_int(message,sys.argv[1])

try:
    print(mymodule.f_to_c(temp))
except:
    print("No valid input")
    exit(99)
