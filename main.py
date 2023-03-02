from art import logo
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)


def main():
    print(logo)

    bids = {}
    is_running = True

    while is_running:
        bidder = input('What is your name?: ').capitalize()
        bid = int(input('What is your bid?: $'))
        entry = {'bidder': bidder, 'bid': bid}
        bids['entry'] = entry

        again = input(
            'Are there any other bidders (Type \'yes\' or \'no\')?: ')
        if again == 'no':
            is_running = False

        clear()

    winner = ''
    max_bid = 0

    for entry in bids.values():
        if entry["bid"] > max_bid:
            winner = entry["bidder"]
            max_bid = entry["bid"]

    print(f'The winnder is {winner} with a bid of ${max_bid}')


if __name__ == '__main__':
    main()
