import colors
import random

def coin_toss:
    coin_sides = ('heads', 'tails')
    result = random.choice(coin_sides)
    user_guess = input('Heads or Tails? ').lower().strip()
    if result[0] == user_guess[0]:
        print(f"You win it was {result}")
    else:
        print(f"You lose, sorry, it was {result}")
    del result

if __name__ == '__main__':
    do_continue = True
    while do_continue:
        coin_toss()
        answer = input('Do you want to spin again? ').lower().strip()
        if answer[0] == 'no'
            do_continue = False