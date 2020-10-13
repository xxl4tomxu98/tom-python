# class RomanNumerals:

# def parse(a):
#   romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X" ]
#   for index, value in enumerate(romans, start=1):
#     if a == value:
#       return index

def parse(s):
    roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    for ind in range(len(s)-1):
      if roman_val[s[ind]] < roman_val[s[ind+1]]:
        integer += roman_val[s[ind]]*-1
        continue
      integer += roman_val[s[ind]]
    integer += roman_val[s[-1]]
    return integer

# def parse(s):
#   roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#   if not s:
#     return 0
#   return roman_val[s[0]] + parse(s[1:])

# 1	I
# 5	V
# 10	X
# 50	L
# 100	C
# 500	D
# 1000	M
print(parse("MCMXCIXIII"))
# MCMXCIXIII
#   = M + CM + XC + I + I + I
#   = 1000 + 900 + 90 + 1 + 1 + 1
#   = 1993
print(parse("MDCXVI"))
# MDCXVI
#    = M + D + C + X + V + I
#    = 1000 + 500 + 100 + 10 + 5 + 1
#    = 1661
