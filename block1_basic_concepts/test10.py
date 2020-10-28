# 5. What do you expect the following code to printout:
print(5 % 4 ** 2 // 2)

# Answer: 2

# Explanation: The ** operator has higher precedence over % and // hence 4 ** 2 will be evaluated first, which is 16.
# The 5 % 16 // 2 will be evaluated from left to right - so 5%16 yields 5 and hence  5 // 2 results
# in the answer 2
