# read two things from the keyboard
# convert to ints and add
# print the result
# what happens if the input is "abc"? we get an error
# add error handling so it doesn't crash on bad data


alpha = input("Enter your favorite number: ")
beta = input ("Enter your least favorite number: ")
try:
    alpha = int(alpha)
except ValueError:
    print("Please enter numeric data")
try:
    beta = int(beta)
except ValueError:
    print("Please enter numeric data")
kappa = alpha + beta
print(kappa)

delta = input("Enter your favorite number: ")
nu = input("Enter your least favorite number: ")
zeta = " "
try:
    zeta = int(delta) + int(nu)
except ValueError:
    print("Please enter numeric data")
print(zeta)

