# What will happen if the following snippet of code is executed?
def greeting(name=""):
    print("Hello", name)

greeting()

# Answer: Hello
# Explanation: The greeting is expecting a name argument but the function
# has a default argument provided to the function parameter. Hence, although
# the greeting() is not providing an argument, the calling of the function
# will not fail
