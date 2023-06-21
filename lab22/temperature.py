import argparse
import momodule

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--fahr', help='Enter Fahrenheit value', type=int)
args = parser.parse_args()

if args.fahr:
    c = f_to_c(args.fahr)
    print(f'Centigrade: {c:.2f}')

