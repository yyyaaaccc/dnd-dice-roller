
# Summary

![roll.py logo](/assets/images/d20_small.png)  
Roll the specified dice and return the result as a string.

# Parameters

The dice parameter should be in the format 'NdS' where N is the number of
dice to roll (defaulting to 1 if omitted) and S is the number of sides on
each die. 

If a numeric value is specified after the dice parameter (e.g. '2d6+3'),
that value is added to the total roll value. The result string shows the
total roll value followed by the added value. For example, '2d6+8' might
return '2d6: 3+5+8 = 16'.

For example: 
- 'd20' rolls a 20-sided die once
- '2d6' rolls two 6-sided dice and returns the sum of the results.
- static value can be added to each rolled dice, e.g. 'd20+2'

# Example usage and results

### python roll.py d20

`d20: 15 = 15`

### python roll.py 1d100

`1d100: 27 = 27`

### python roll.py d20+4 2d6+3 d4+1

`d20+4:	8 +4 = 12`  
`2d6+3:	1+2 +3 = 6`  
`d4+1:	3 +1 = 4`   



