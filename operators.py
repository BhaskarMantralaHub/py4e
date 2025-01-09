# Operator precedence (PEMDAS)
# Left to right

# Parenthesis
# Exponent / Power (**)
# Division / Multiplication / Modulus - Left to right
# Addition / Subtraction - Left to right
print (1 + 2**3 / 4 * 5 / (10 * 2))

# 1. Brackets - 10 * 2 -> 20
# 2. Power -> 2**3 -> 8
# 2. Division -> 8/4 -> 2 (left to right)
# 3. Multiplication -> (1 + 8/4 * 5 / 20) -> (1 + 10 / 20)
# 4. Division -> (1 + 0.5)
# 5. Addition -> 1.5


print (1 + 2 * 3 - 8 / 4)

# 2*3 -> 6
# 8/4 -> 2.0
# 1+ 6 -> 7
# 7 - 2.0 -> 5.0

print (int(98.6)) #Flooring