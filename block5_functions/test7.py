# What is the output of the following code

def fun(a = 3, b = 2):
    return b ** a

print(fun(2))

# Answer: 4
# Explanation: The function expects two values, but if not provided,
# they can be defaulted to 3 and 2 respectively for a and b.
# Note that he function calculates and returns b to the power of a.
# When you call the function with one value, we are setting a using the positional argument
# while the value b is defaulted to 2.
