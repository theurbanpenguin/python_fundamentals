import argparse
import mymodule

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--fahr', help='Enter Fahrenheit value', type=int)
parser.add_argument('-c', '--cent', help='Enter Centigrade value', type=int)
args = parser.parse_args()

if args.fahr:
    c = f_to_c(args.fahr)
    print(f'Centigrade: {c:.2f}')
if args.cent:
    f = c_to_f(args.cent)
    print(f'Fahrenheit: {f:.2f}')
