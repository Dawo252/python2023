""" Zad1 """

if_ex_1 = input("czy chcesz odpalic zad1? y/n \n")

if if_ex_1 == 'y':
    word = input("podaj sowoje slowo:\n")
    actual_sep = input("podaj aktualny separator:\n")
    wanted_sep = input("podaj docelowy separator:\n")

    print(wanted_sep.join(word.split(actual_sep)))

""" Zad2 """

lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz ' \
        'pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później '\
        'zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w ' \
        'latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z ' \
        'zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach ' \
        'osobistych, jak Aldus PageMaker '

surname_letter = 's'
name_letter = 'w'

print(f"w tekscie jest: {lorem.count(surname_letter)} liter {surname_letter} oraz {lorem.count(name_letter)} liter {name_letter}")

""" Zad3 """
one, two = 'one', 'two'

print(f'{one} {two}')
print(f'{1} {2}')

print(f"{'test':>10}")
print(f"{'test':10}")
print(f"{'test':_<10}")
print(f"{'test':^10}")
print(f"{'zip':^6}")

print(f"{42:04d}")
print(f"{42:+d}")
print(f"{42:=+5d}")
print(f"{42:=-5d}")