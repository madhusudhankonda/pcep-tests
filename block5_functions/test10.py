# What is the output of the following code:
def func1():
    print("func1")
    def func2():
        print("func3")
        def func3():
            print("func3")
        func3()
    func2()
func1()

# Answer:
# func1
# func3
# func3

# Explanation: The nested function1 will call the second function which in
# turn calls the third function


