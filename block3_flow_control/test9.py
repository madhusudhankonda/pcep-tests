# What will be the output of the following code:
nums = [[1, 2, 3]]
initializer = 1

for i in range(1):
    initializer *= 10
    for j in range(1):
        nums[i][j] *= initializer

print(nums)
# Answer: [[10, 2, 3]]

# Explanation: The nums is a two-dimensional list. The code consists of
# range(1) so the loop is executed once only with 0 value. The new values of
# the initializer is set to 10 as it was multiplied by 10. The nums[i][j] is
# nothing but nums[0][0] which is set to the new initializer
