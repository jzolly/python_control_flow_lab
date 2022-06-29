# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
choice = input(' "Please enter a letter from a-z" ').lower()
print(f'The user entered {choice}')


letter_selection = ''
if choice.isalpha() and len(choice) == 1:
    letter_selection = choice
else:
    print(f'{choice} must be a single character from a-z')  

# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

if letter_selection == "a" or letter_selection == "e" or letter_selection == "i" or letter_selection == "u" or letter_selection == "o":
    print(f'{letter_selection} is a vowel')
else:
    print(f'{letter_selection} is a consonant')



# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':




# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 

# phrase = input('Hello please enter a "phrase" or "word" ')

# 2. Print the following message:
#      - What you entered is xx characters long

# print(f'Your phrase, "{phrase}", is {len(phrase)} characters long.')

# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ""
while phrase != 'quit':
    phrase = input('Hello please enter a "phrase" or "word" or type "quit" to exit: ')
    if phrase != "quit":
        print(f'Your entry, "{phrase}", is {len(phrase)} characters long.')
    elif phrase == "quit":
        print('Hope you enjoyed this')
        break
    else:
        print("ERROR. Please enter word or phrase")


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
dog_age_str = input('Please enter your dogs age in humans years: ')
dog_age = None
if dog_age_str.isnumeric():
    dog_age = int(dog_age_str)
# elif dog_age_str.isfloat():  NOTE: figure out float
#     dog_age = float(dog_age_str)
else:
    print('ERROR. Please enter a numeric age for your dog')


# 2. Calculates the equivalent dog years, where:
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
if dog_age > 2:
    dog_age = (dog_age - 2) * 7 + 20
    print(f'Your dog is {dog_age} years old in dog years.')
else:
    dog_age *= 10
    print(f'Your pup is {dog_age} years old in dog years.')
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each



# Hint:  Use the int() function to convert the string returned from input() into an integer


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
side_a = None
side_b = None
side_c = None
# If time, put in a while loop so that the triangle type function doesn't run until all sides are verified numbers.  Also handle floats
side_a_str = input('Enter triangle length for "side a": ')
if side_a_str.isnumeric():
    side_a = int(side_a_str)
else:
    print('ERROR. Please enter a number')

side_b_str = input('Enter triangle length for "side b": ')
if side_b_str.isnumeric():
    side_b = int(side_b_str)
else:
    print('ERROR. Please enter a number')

side_c_str = input('Enter triangle length for "side c": ')
if side_c_str.isnumeric():
    side_c = int(side_c_str)
else:
    print('ERROR. Please enter a number')

print(f'side a = {side_a}')
print(f'side b = {side_b}')
print(f'side c = {side_c}')

triangle_type = ''

if side_a == None or side_b == None or side_c == None:
    print('ERROR.  One or more of your sides are not a number. Try again.') 
elif side_a == side_b and side_a == side_c:
    triangle_type = 'equalateral'
    print(f'All sides are equal, you have an {triangle_type}')
elif side_a == side_b or side_a == side_c or side_c == side_b:
    triangle_type = 'isosceles'
    print(f'Two of your sides are the same, you have an {triangle_type}')
else:
    triangle_type = 'scalene'
    print(f'None of your sides are the same, you have a {triangle_type}')





# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
x = range(1, 51)

y = 0
z = 1
fib = 1
for n in x: 
    print(f'term: {n} / number: {fib}')
    fib = y + z
    y = z
    z = fib
# Hint: The next number is found by adding the two numbers before it

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
