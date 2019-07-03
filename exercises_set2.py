# Exercise 1: Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Exercise 2: What is the output of this code?
num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# num[::3] = [0,3,6,9,12,15,18]
# num[::-1] = [19,18,17,16,15,14, etc]
print(num[::3])

# Exercise 3: What is the output of this code?
areas = ["hallway",11.25,"kitchen",18.0,"living room",20.0,"bedroom",10.75,"bathroom",9.50]
# areas.pop(6) = "bedroom"
print(areas.pop(6))

# Exercise 4: What is the output of this code:
areas2 = ["hallway",11.25,"kitchen",18.0,"chll zone",20.0,"bedroom",10.75,"bathroom",10.50,"poolhouse",24.5,"garage",15.45]
# del(areas2[-4:-2]) = 'poolhouse', 24.5
del(areas2[-4:-2])
print(areas2)

# Exercise 5: Grab 'hello'
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Exercise 6: Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# Exercise 7: What is the output of this code? Two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
l_one[2][0] >= l_two[2]['k1']
# Ans: 3 >= 4:  False

# Exercise 8: What is the output of this code?
char = {'a':'1', 'b':'2', 'c':'3'}
char_2 = dict()
for keys,values in char.items():
    print(keys)
    print(values)
    print('\n')

# Exercise 9:


# Exercise 10: Use for, .split and if to create a statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# Exercise 11: Use range() to print all the even numbers from 0 to 10.
for num in range(0,11,2):
    print(num)

# Exercise 12: User a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [num for num in range(1,51) if num%3==0]
print(mylist)

# Exercise 13: Go through the spring below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)

# Exercise 14: