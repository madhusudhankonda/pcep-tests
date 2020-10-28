# What is the output of the following code?

x = 0
y = 1
def swap(x, y):
    z = x
    x = y
    y = z
    return (x, y)

x, y = swap(x, y)
print(x, y)

# Answer: 1 0
# Explanation: The values are swapped in the function and returned
