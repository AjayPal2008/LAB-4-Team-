# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 3 (Team)/(optional)
# Date:         11 September 2026
from operator import eq


A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

equation = ""

if A == -1: equation += "-x^2 "
elif A == 1: equation += "x^2 "
elif A == 0: break
else: equation += str(A)+"x^2 "

if B == -1: equation += "- x "
elif B == 1: equation += "+ x "
elif B>0: equation += "+ "+str(abs(B))+"x "
elif B == 0: break
else: equation += "- "+str(abs(B))+"x "

if C >0: equation+= "+ "+str(C)
elif C == 0: break
else: equation += str(C)

equation += " = 0"

print("The quadratic equation is "+ equation)# Output of equation

