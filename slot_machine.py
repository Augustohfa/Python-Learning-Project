import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    '1': 2,
    '2': 4,
    '3': 6,
    '4': 8,
}
symbol_values = {
    '1': 5,
    '2': 4,
    '3': 3,
    '4': 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    # transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                # to the divider just be in the middles
                print(column[row], end='')
        print()


def deposit():
    while True:
        amount = input('How much would you deposit? \n$')
        if amount.isdigit():
            amount = int(amount)  # transform string into integer
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number!')
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f'Enter the number of lines you want to bet on (1-{MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)  # transform string into integer
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(
                    f'The number of lines must be greater than - and lesser than {MAX_LINES}!')
        else:
            print('Please enter a number!')
    return lines


def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)  # transform string into integer
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a number!')
    return amount


def spin(user_balance):
    lines_bettet_on = get_number_of_lines()
    while True:
        user_bet = get_bet()
        total_bet = user_bet * lines_bettet_on

        if total_bet > user_balance:
            print(
                f'You do not have this amount in yout balance. '
                f'Your current balance is: ${user_balance}'
            )
        else:
            break
    print(
        f'You are betting ${user_bet} on {lines_bettet_on} lines! \n'
        f'Total bet is ${total_bet}!'
    )
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(
        slots, lines_bettet_on, user_bet, symbol_values)
    print('You won on line: ', *winning_lines)
    print(f'You won ${winnings}!')
    return winnings - total_bet


def main():
    user_balance = deposit()
    while True:
        print(f'Current balance is ${user_balance}')
        awnser = input('Press enter to spin(q to quit)')
        if awnser == 'q':
            break
        user_balance += spin(user_balance)
    print(f'You left with ${user_balance}')


main()
