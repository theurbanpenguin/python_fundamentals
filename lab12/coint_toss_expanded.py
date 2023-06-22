# A simple heads or tails game emulating a coin toss
# First we create a set. This is a special list that is unordered
# This means the ordering of the set elements in not fixed
sides = {'heads', 'tails'}

# As the ordering in not fixed, elements of a set are not addressable directly
# We could print(side) and the complete set will show in a ransom order on each execution
# Ideally, we want just heads or tails to print
# For this we convert the generated set into a list. The set is randomly generated on each execution
# We can then pull out the first element ( index 0 )

result = list(sides)[0]

# Let's ask the user for their choice
# We ensure the user choice is stored in the variable in lower case to match the case in the set
user = input('Heads or Tails?: ').lower()

# We can test the selection now, using format printing we can easily add the variables
# For added color we can set variables for the color output
# As we only use the values one, we don't need the color variables
# However it is easier than embedding the codes in the text
# We need the reset code the clear the color formatting

red   = '\033[31m'
green = '\033[32m'
reset = '\033[0m'

if result == user:
    print(f'{green}You win, it was {result}{reset}')
else:
    print(f'{red}You lose, it was {result}{reset}')
