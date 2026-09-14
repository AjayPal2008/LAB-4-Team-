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
# Date:         14 September 2026
#

nickel = 0.05
quarter = 0.25
dime = 0.10
penny = 0.01

x = float(input("How much did you pay? "))
y = float(input("How much did it cost? "))
change = round(x - y, 2)

quarters, change = divmod(change, quarter)
dimes, change = divmod(change, dime)
nickels, change = divmod(change, nickel)
pennies, change = divmod(round(change, 2), penny)

print(f"You received ${x - y:.2f} in change. That is ...")
print(f"{int(quarters)} quarter(s), {int(dimes)} dime(s), "
	f"{int(nickels)} nickel(s), and {int(pennies)} penny/pennies.")
