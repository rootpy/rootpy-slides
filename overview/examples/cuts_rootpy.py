# test
from rootpy.tree import Cut

cut1 = Cut('a < 10')
cut2 = Cut('b % 2 == 0')

cut = cut1 & cut2
print cut

# expansion of ternary conditions
cut3 = Cut('10 < a < 20')
print cut3

# easily combine cuts arbitrarily
cut = ((cut1 & cut2) | - cut3)
print cut
