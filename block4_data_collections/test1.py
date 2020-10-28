# What do you expect when the following code snippet is run:
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday")
weekdays.append("Friday")
print(weekdays)
# Answer: AttributeError: 'tuple' object has no attribute 'append'
# Explanation: Tuples are immutable and can't be amended once created
