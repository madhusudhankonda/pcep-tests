# How many times will it print"#"?
x=10
if x < 10:
    print("#")
    if x<8:
        print("#")
    elif x==10:
        print("#")
    else:
        print("#")
else:
    print("#"*3)

# Answer: ###

# Explanation: The outer most if statement is false as x is not less than 10
# (it is equal to 10), hence the else block will be executed.
# The string * number will result in number of times the string being printed
# out. Hence ### is correct.
