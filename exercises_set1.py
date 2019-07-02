# Exercise: 1 ( basic print function). print out the phrase "Hello World".
# Print this by using a variable and also print without using a variable.

mystring = "Hello World"
print(mystring)

print("Hello World")

# Exercise 2: Write an expression that equals 100.
# For example 50 + 50 or 110 - 10
print((((4 + 12)/2) **2) + 80 - 44)

# Exercise 3: Which of these is a floating point number? A: 5.6; B: 200, C:4.0
# Ans: A & C:
print(type(5.6))
print(type(200))
print(type(4.0))

# Exercise 4: What is the output of 6*6
print(6*6)

# Exercise 5: String Indexing
# Write a string index that returns just the letter 'r' from 'Hello World'. Example 'Hello World[0]' returns 'H'
mystring2 = 'Hello World'
print(mystring2[8])

# Exercise 6: String Slicing
# Use string slicing to grab the word 'ink' from inside 'tinker'. For example, 'education'[3:6] returns 'cat'
mystring3 = 'tinker'[1:4]
print(mystring3)

# Exercise 7:
# If s='hello' what is the output of s[1]? Ans: e
# If s='Sammy' what is the output of s[2:]? Ans: mmy

# Exercise 8: What is the result of this print statement?
# print('The {} {} {}'.format('fox','brown', 'quick'))
# Ans: The fox brown quick

# Exercise 9: Using f-strings, print out the value of the following phrase using the variables given below:
# "I love python"
Name1 = "love"
Name2 = "python"
print(f"I {Name1} {Name2}")

# Exercise 10: Write the expression to find the following: The output should match what is shown below.
# What is 7 to the power of 4?
print(7**4)

# Exercise 11: I know we have not covered lists, but this is a string exercise,
# so don't worry too much about the list part. The method to use for this is a string method.
# Split this string into a list:
s = "Hi there Sam!"
print(list(s.split()))

# Exercise 12: What Boolean will be the output of the following:
print(2 < 4)

# Exercise 13: What Boolean will be the output of the following?
a = 12
b = a - 10
print(a > b)

# Exercise 14: What Boolean will be the output of the following?
# What Boolean will be the output of the following: 12 != 12