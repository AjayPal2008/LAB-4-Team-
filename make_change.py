# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 4 (Team)
# Date:         11 September 2026

#Values of each coin
nickel = 0.05
quarter = 0.25
dime = 0.10
penny = 0.01

x = float(input("How much did you pay? "))
y = float(input("How much did it cost? "))
change = round(x - y, 2)

if change < 0:
    print("Error: amount paid is less than the cost.")
else:
    quarters = int(change / quarter)
    change = round(change - quarters * quarter, 2)
    dimes = int(change / dime)
    change = round(change - dimes * dime, 2)
    nickels = int(change / nickel)
    change = round(change - nickels * nickel, 2)
    pennies = int(change / penny)

    print(f"You received ${x - y:.2f} in change. That is...")
    if quarters > 0:
        name = "quarter" if quarters == 1 else "quarters"
        print(f"{quarters} {name}")

    if dimes > 0:
        name = "dime" if dimes == 1 else "dimes"
        print(f"{dimes} {name}")

    if nickels > 0:
        name = "nickel" if nickels == 1 else "nickels"
        print(f"{nickels} {name}")

    if pennies > 0:
        name = "penny" if pennies == 1 else "pennies"
        print(f"{pennies} {name}")
