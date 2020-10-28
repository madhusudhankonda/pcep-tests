# What do you expect to get printed when the following code is executed
# when user enters 'wi' and 'fi' for a and b when prompted:
a = input()
b = input()

print(a + b * 3)

# Answer: wifififi

# Explanation: The * operator takes precedence over + operator, so b*3
# will be evaluated first, resulting in fififi. This is then concatenated
# to the variable a's value, resulting in wifififi

