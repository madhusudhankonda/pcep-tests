# What is the output when the following code is executed:
lst1 = [0, 1]
lst2 = [1, 0]
for x in lst1:
    for y in lst2:
        print(x, y)

# 0 1
# 0 0
# 1 1
# 1 0

# Explanation: For each of the element in list1, every element in the list2
# will be printed. Hence 0, 1 and 0, 0 in the first iteration; 1 1,1 0 in
# the second iteration
