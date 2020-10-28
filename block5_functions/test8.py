# What do you expect the output would be:
x = 100
def glob():
   global x
   x = 20
glob()
print(x)
# Answer:20
# Explanation:The variable x is global which means it can be used inside a
# function without defining it in the function. When you change the value
# inside the function it affects the value outside too, hence when it's
# printed outside the function, the new value will come in affect.


