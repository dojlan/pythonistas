from math import pi
def vol(rad):
    return (4/3) * pi * rad**3

print(vol(2))

def ran_check(num,low,high):
    if num in range(low, (high + 1)):
        return(f"{num} is in the range between {low} and {high}")

print(ran_check(2, 2, 7))

def ran_bool(num2,low2,high2):
    return num2 in range(low2, (high2 + 1))

print(ran_bool(3,1,10))


def up_low(s):
    upper_letters = 0
    lower_letters = 0
    for letter in s:
        if letter.isupper():
            upper_letters += 1
        elif letter.islower():
            lower_letters += 1
    print(f"No of Upper case characters : {upper_letters}")
    return (f"No of Lower case characters : {lower_letters}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))


def unique_list(lst):
    return set(lst)

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(multiply([1,2,3,-4]))

def palindrome(s):
    return s[::] == s[::-1]

print(palindrome('helleh'))

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    mystring = ''.join(set(str1.lower().split()))
    for letter in alphabet:
        if letter not in mystring:
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))

str1 = "The quick brown fox jumps over the lazy dog"
def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(str1.lower())
    #print(set(alphabet))
    #print(set(str1.lower()))

print(ispangram("The quick brown fox jumps over the lazy dog"))