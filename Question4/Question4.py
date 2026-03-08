from fractions import Fraction

p = {25: Fraction(1,1), 26: Fraction(0,1)}
for m in range(24, 0, -1):
    p[m] = Fraction(1,2)*p[m+1] + Fraction(1,2)*p[m+2]

print(p[1], float(p[1]))
