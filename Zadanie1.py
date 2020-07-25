from sys import argv
def calc():
    try:
        money, hours, bonus = map(int, argv[1:])
        print(f"Зарплата - {money*hours+bonus}")
    except ValueError:
        print("Enter correct numbers.")
calc()