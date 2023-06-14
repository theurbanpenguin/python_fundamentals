from sys import argv
import mymodule

file = mymodule.basename(argv[0])
message = file + ': Enter a temperature to convert as an integer: '

if len(argv) > 1:
    try:
        temp = int(argv[1])
    except ValueError:
        temp = mymodule.prompt_for_int(message, argv[1])
    finally:
        print(mymodule.f_to_c(temp))
