import random
import re
import sys

def roll_dice(dice):
    # Parse the dice parameter using regular expressions
    match = re.match(r'^(\d*)d(\d+)$', dice)
    if not match:
        raise ValueError('Invalid dice parameter: {}'.format(dice))
    count = int(match.group(1) or 1)
    sides = int(match.group(2))
    # Roll the dice and return the result
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)
    result = '{}: {}'.format(dice, '+'.join(str(r) for r in rolls))
    result += ' = {}'.format(total) if count > 1 else ''
    return result

if __name__ == '__main__':
    # Parse command-line arguments and roll the dice
    for dice in sys.argv[1:]:
        try:
            result = roll_dice(dice)
            print(result)
        except ValueError as e:
            print(e, file=sys.stderr)