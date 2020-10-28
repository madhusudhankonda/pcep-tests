# What do you expect the following code to print:
nums = [1, 2, 3]
for i in range(len(nums)):
    nums.insert(i, i+1)
print(nums)

# Answer: [1, 2, 3, 1, 2, 3]
# Explanation: The loop iterates over the length of the list (3)
# and then the insert() adds 1,2,3 values at 0,1,2 indices, moving up the existing list elements' positions
