import sys
from builtins import print

print("Please enter your number..")
x="Input"
ans = input(f'WARNING!!! The script will decide your number from "{x}". Are you sure to continue? (Y/N): ')
if ans != 'Y':
    print("We will not provide you the details as you regret the request...")
    sys.exit(0)
input1 = input("Enter here ")
if input1 != '21':
    print("The number you have entered is not your lucky number...")
    sys.exit(0)
else:
    print("Your lucky number is "+input1)
print()
print("end of the class")