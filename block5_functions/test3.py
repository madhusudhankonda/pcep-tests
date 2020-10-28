# What is the output of the following code:

def put(x):
   x[-1] = 6
val = [0, 1, 2, 3, 4, 5]
put(val)
print(val)

# Answer:[0, 1, 2, 3, 4, 6]
# Explanation: Even though the function doesn't return anything, it does
# change the value of the list which can be accessed outside the function too
