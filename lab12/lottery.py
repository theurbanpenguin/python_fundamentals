import random


def generate_uk_lottery_numbers():
    # Generate a list of numbers from 1 to 59
    all_numbers = list(range(1, 60))

    # Shuffle the list to randomize the order
    random.shuffle(all_numbers)

    # Take the first 6 numbers from the shuffled list
    lottery_numbers = all_numbers[:6]

    return sorted(lottery_numbers)


if __name__ == "__main__":
    unique_numbers = generate_uk_lottery_numbers()
    print("Your unique UK National Lottery numbers are:", unique_numbers)

