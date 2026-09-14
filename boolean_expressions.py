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
a =  input().lower() == "t" or input().lower() == "f" or input().lower() == "true" or input().lower() == "false"
print("Enter True or False for b: ")
b = input().lower() == "t" or input().lower() == "f" or input().lower() == "true" or input().lower() == "false"
print("Enter True or False for c: ")
c = input().lower() == "t" or input().lower() == "f" or input().lower() == "true" or input().lower() == "false"
############ Part B ############ 
print("a and b and c: ",a and b and c)
print("a or b or c: ",a or b or c)
############ Part C ############ 
XOR1 = a!=b
print("XOR:",XOR1)
print((b==c) or (b==a) or (a==c) or not(a==b and b==c and c==False))
############ Part D ############ 
Complex_1 = (not (a and b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
Complex_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

Simple_1 = (not b) or (not a and not c)
Simple_2 = (a or ((not b) and c))

print("Complex 1:", Complex_1)
print("Simple 1:", Simple_1)
print("Complex 2:", Complex_2)
print("Simple 2:", Simple_2)
