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