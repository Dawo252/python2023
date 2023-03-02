""" Zad 1 """

print(int('1101', 2))  # -> 13
print(float(11))
print(float('15.6754'))

""" Zad 2 """

number_int = 13  # -> 1101
print(number_int.bit_count())  # -> 3

float_number = 100.0
float_number_not_integer = 100.7
print(float_number.is_integer())
print(float_number_not_integer.is_integer())

""" Zad 3 """
""" tabelka sprawdzająca dla podstawowych operacji bitowych"""

for i in range(2):
    for j in range(2):
        print(f'{i, j} -> AND => {i & j}')
        print(f'{i, j} -> OR =>{i | j}')
        print(f'{i, j} -> XOR =>{i ^ j}')

x = 9  # 0b1001

print(x << 1)
print(bin(x << 1))

print(x >> 1)
print(bin(x >> 1))
