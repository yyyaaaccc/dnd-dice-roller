import random
import re
import sys

def roll_dice(dice):
    """
    Roll the specified dice and return the result as a string.

    The dice parameter should be in the format 'NdS' where N is the number of
    dice to roll (defaulting to 1 if omitted) and S is the number of sides on
    each die. For example, 'd20' rolls a 20-sided die once, while '2d6' rolls
    two 6-sided dice and returns the sum of the results.

    The result string shows each result of the roll concatenated by "+" and
    summarized as total roll value. For example, '2d6' might return '2d6: 3+5 = 8'.
    If only one die is rolled, the result string shows only the total roll value.

    If a numeric value is specified after the dice parameter (e.g. '2d6+3'),
    that value is added to the total roll value. The result string shows the
    total roll value followed by the added value. For example, '2d6+3' might
    return '2d6: 3+5+3 = 11'.
    """
    # Parse the dice parameter and added value using regular expressions
    match = re.match(r'^(\d*)d(\d+)(?:\+(\d+))?$', dice)
    if not match:
        raise ValueError('Invalid dice parameter: {}'.format(dice))
    count = int(match.group(1) or 1)
    sides = int(match.group(2))
    added = int(match.group(3) or 0)
    # Roll the dice and return the result
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + added
    # Build the result string
    result = '{}: {}'.format(dice, '+'.join(str(r) for r in rolls))  # Add the dice notation and the individual rolls
    result += ' = {}'.format(total)  # Add the total roll value 
    return result

if __name__ == '__main__':
    # Parse command-line arguments and roll the dice
    for dice in sys.argv[1:]:
        try:
            result = roll_dice(dice)
            print(result)
        except ValueError as e:
            print(e, file=sys.stderr)