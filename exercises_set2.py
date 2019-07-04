# Exercise 1: Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Exercise 2: What is the output of this code?
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# num[::3] = [0,3,6,9,12,15,18]
# num[::-1] = [19,18,17,16,15,14, etc]
print(num[::3])

# Exercise 3: What is the output of this code?
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# areas.pop(6) = "bedroom"
print(areas.pop(6))

# Exercise 4: What is the output of this code:
areas2 = ["hallway", 11.25, "kitchen", 18.0, "chll zone", 20.0, "bedroom", 10.75, "bathroom", 10.50, "poolhouse", 24.5,
          "garage", 15.45]
# del(areas2[-4:-2]) = 'poolhouse', 24.5
del (areas2[-4:-2])
print(areas2)

# Exercise 5: Grab 'hello'
d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Exercise 6: Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))

# Exercise 7: What is the output of this code? Two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
# True or False?
l_one[2][0] >= l_two[2]['k1']
# Ans: 3 >= 4:  False

# Exercise 8: What is the output of this code?
char = {'a': '1', 'b': '2', 'c': '3'}
char_2 = dict()
for keys, values in char.items():
    print(keys)
    print(values)
    print('\n')

# Exercise 9:
# 1.Print out the values of each city’s index in the superdict dictionary below.
# Note that the keys of the outer dictionary corresponds to the index.
# 2. Print out each city name in the dictionary
# 3. What is the out put of this code:
print(" two of the cities in the list are {0} and {1}".format(el[0], el[1]))

superdict = {
    '1': {
        'city': 'pittsburgh',
        'wins': '6'
    },
    '2': {
        'city': 'Dallas',
        'wins': '5'
    },
    '3': {
        'city': 'San Francisco',
        'wins': '4'
    },
    '4': {
        'city': 'New York',
        'wins': '7'
    },
    '5': {
        'city': 'Denver',
        'wins': '3'
    },
    '6': {
        'city': 'Miami',
        'wins': '2'
    }
}

# Exercise 10: Use for, .split and if to create a statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# Exercise 11: Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11, 2):
    print(num)

# Exercise 12: User a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [num for num in range(1, 51) if num % 3 == 0]
print(mylist)

# Exercise 13: Go through the spring below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)


# Exercise 14:
# See exercises_set1

# Exercise 15:
# See exercises_set1

# Exercise 16: Define a function called is_even that takes in one argument, and returns True if the passed-in
# value is even, False if it is not.
def is_even(num):
    return num % 2 == 0

print(is_even(8))

# Exercise 17: BMI Calculator
# Write a function that calculates the BMI of a person. The function must also tell the user the following;
#  -> You are overweight if BMI is greater than 25
#  -> Otherwise "You are in top shape"
def ur_bmi(ur_weight, ur_height):
    # ur_weight in kg and ur_height in meters
    bmi = ur_weight/(ur_height**2)
    if bmi > 25:
        print(f"Your BMI is {bmi} and you are overweight")
    else:
        print("You are in top shape")

ur_bmi(82,1.70)

# Exercise 18: ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words
# begin with the same letter.
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(mystring):
    return mystring.split()[0][0] == mystring.split()[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# Exercise 19: MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the
# integers is 20. If not, return False.
# -> makes_twenty(20,10) --> True
# -> makes_twenty(12,8) --> True
# -> makes_twenty(2,3) --> False
def makes_twenty(num1,num2):
    return (num1 + num2) == 20 or num1 == 20 or num2 == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# Exercise 20: OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# -> old_macdonald('macdonald') --> MacDonald
# -> Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(mystring):
    return mystring[:3].capitalize() + mystring[3:].capitalize()

print(old_macdonald('macdonald'))


# Exercise 21: FIND 33: Given a list of ints, return True if the array contains a 3 next a 3 somewhere.
# -> has_33([1,3,3]) --> True
# -> has_33([1,3,1,3]) --> False
# -> has_33([3,1,3]) --> False
def has_33(mylist):
    pass
#    for num in range(len(mylist)):
#        if mylist[num] == 3 and mylist[num + 1] == 3:
#            print("Twins")
#        else:
#            print("Tall")

#print(has_33([1,3,1,1]))

# Exercise 22: PAPER DOLL: Given a string, return a string where for every character in the original
# there are three characters.
# -> paper_doll('Hello') --> 'HHHeeellllllooo'
# -> paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'
def paper_doll(mystring):
    nustring = ''
    for letter in mystring:
        nustring += letter*3
    return nustring

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# Exercise 23: BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# -> blackjack(5,6,7) --> 18
# -> blackjack(9,9,9) --> 'BUST'
# -> blackjack(9,9,11) --> 19
def blackjack(num1,num2,num3):
    if (num1+num2+num3) <= 21:
        return num1+num2+num3
    elif num1+num2+num3 > 21 and (num1==11 or num2==11 or num3==11):
        if (num1+num2+num3 - 10) > 21:
            return 'BUST'
        else:
            return (num1+num2+num3) - 10
    else:
        return 'BUST'

print(blackjack(11,11,11))


# Exercise 24: SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers
# with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# -> summer_69([1, 3, 5]) --> 9
# -> summer_69([4, 5, 6, 7, 8, 9]) --> 9
# -> summer_69([2, 1, 6, 9, 11]) --> 9
def summer_69(arr):
    pass


# Exercise 25: SPY GAME: Write a function that takes in a list of integers and returns True if it contains
# 007 in order
# -> spy_game([1,2,4,0,0,7,5]) --> True
# -> spy_game([1,0,2,4,0,5,7]) --> True
# -> spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    pass


# Exercise 26: You are driving a little too fast, and a police officer stops you. Write a function to
# return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60
# or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket".
# If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value
# in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def speed_check(speed, birthday_value):
    if speed <= 60 or (speed <= 65 and birthday_value):
        return "No ticket"
    elif 61 <= speed <= 80 or (speed <= 85 and birthday_value):
        return "Small ticket"
    else:
        return "Big Ticket"

print(speed_check(86,True))


# Exercise 27: Write a Python function that accepts a string and calculates the number of uppercase
# and lowercase letters
# See exercises_set1


# Exercise 28: Write a Python function that takes a list and returns a new list with unique elements of
# the first list.
# -> Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# -> Unique List : [1,2,3,4,5]
def unique_list(lst):
    return set(lst)

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# Exercise 29: Write a Python function that checks whether a passed in string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g
# madam, nurses run
def palindrome(s):
    if s[::] == s[::-1]:
        return s

print(palindrome('madam'))


# Exerise 30: Write a Python function to check whether a string is pangram or not.
# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example: "The quick brown fox jumps over the lazy dog"
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter not in str1:
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))


# Exercise 31: Write the following function as a lambda expression:
# def test(x):
#     if x%2==0:
#         return x**2
#     else:
#         return x+3


 # Exercise 32: Use lambda function to filter out words that start with letter 's' in seq:
 # seq = ['soup', 'dog', 'salad', 'cat', 'great']
 # Hint: (use filter with lambda)


# Exercise 33:
# Using a lambda function print out the first letters of the words in the following list
# names = ['Andy', 'Eve', 'Sally']
# Hint ( use map with lambda)


# Exercise 34:
# What is the output of this function. ( try and do this mentally)
# def func(alfa):
#    beta = list(map(lambda x:x-1, alfa))
#    return len(list(filter(lambda y:y%3==0, beta)))
# print(func(range(1,10)))


# Exercise 35:
# What is the output of this code: ( do this mentally—first)
# what = """1"""
# up = '1'
# print(what is up)


# Exercise 36:
# What is the output of this code ( Try it mentally)
a = [1,2,3,4,5]
s = 0
for i in a[:3]:
    for j in a[3:]:
        s += 1
print(s)


# Exercise 37:
# What is the output of this code:

a = list(range(2,10,2))
b = list(range(3,10,3))

# Ans: {3,9}
print(set(b)- set(a))


# Exercise 38:
# a, b, *c = [1,2,3,4,5,6,7,8,9]
# What is the value of a, b and c

# Exercise 39:
# What is the output of this code ( try it mentally first)
d= dict(searchcriteria={"name": "10004"},
        returnedtags={"name": "james", "desc": "Test"})
print(d)

# Exercise 40:
# What is the output of this code
x = [1,[2,[3,4],5],6]
print(x[1][1][1])
print(len(x))
