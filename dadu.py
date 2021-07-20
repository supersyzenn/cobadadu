import random

dice = {}


def roll(sides=6):
    lempardadu = random.randint(1, sides)
    return lempardadu


def main():
    putar = True
    while putar:
        angka = roll()
        tanya = input("Ingin Melempar Dadu? (y/n)")
        if tanya.lower() != "n":
            if angka in dice:
                dice[angka] += 1
            else:
                dice[angka] = 1
            print("Angka Dadu yang keluar :", angka)
        else:
            putar = False
            for angka in range(1, 7):
                print("Angka", str(angka), "keluar", str(dice[angka]), "kali.")


main()
