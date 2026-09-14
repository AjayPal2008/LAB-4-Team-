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

############ Part A ############ 
print("Enter True or False for a: ")
a = input().lower() == "true" or input().lower() == "false"
print("Enter True or False for b: ")
b = input().lower() == "true" or input().lower() == "false"
print("Enter True or False for c: ")
c = input().lower() == "true" or input().lower() == "false"
############ Part B ############ 
print("a and b and c: ",a and b and c)
print("a or b or c: ",a or b or c)
############ Part C ############ 
XOR1 = a!=b
print("XOR",XOR1)
############ Part D ############ 
