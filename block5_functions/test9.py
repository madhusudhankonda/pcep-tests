# What do you expect the following program to print to the console when executed?

def tripler(num):
    def doubler(num):
        return num *2
    num = doubler(num)
    return num * 3

print(tripler(2))

# Answer: 12

# Explanation: The tripler calls doubler with the passed in 2 as the argument.
# The doubler doubles the number and returns the result. The returned result
# is then reassigned to the num which is then tripled and printed out
