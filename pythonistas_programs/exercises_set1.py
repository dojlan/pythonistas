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
# 12 != 12 Ans: False

# Exercise 15: What Boolean will be the output of the following?
# 2 < 3 <10  Ans: True

# Exercise 16: User for, split() and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# Exercise 17: User range() to print all the even numbers from 0 to 10.
for num in range(0,11,2):
    print(num)

# Exercise 18: Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [num for num in range(0,51,3) if num % 3 == 0 ]
print(mylist)

# Exercise 19: Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)

# Exercise 20: Write a program that prints the integers from 1 to 100. But for multiples of three, print "Fizz"
# instead of the number, and for multiples of five print "Buzz". For numbers which are multiples of three and
# five, print "FizzBuzz".
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# Exercise 21: Use List Comprehension to create a list of the first letters of every word in the string below;
st = 'Create a list of the first letters of every word in this string'
mylist = [word[0] for word in st.split()]
print(mylist)

# Exercise 22: Write a program to count how many upper case and lower case letters in this string
st = "Hello Mr. Rogers, how are you this fine Tuesday"
# Output should be:
# Uppercase: 4
# Lowercase: 33

Uppercase = 0
Lowercase = 0
for num in range(len(st)):
    if st[num].isupper():
        Uppercase += 1
    elif st[num].islower():
        Lowercase += 1
print(Uppercase)
print(Lowercase)

# Completion of exercises