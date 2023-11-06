#ques 1
# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate nCr
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

# Function to calculate GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Function to calculate LCM
def lcm(n, r):
    return n * r // gcd(n, r)

# Open the file
with open('Assign5_1.txt', 'r+') as file:
    lines = file.readlines()  # Read all lines
    file.seek(0)  # Go back to the start of the file
    file.truncate()  # Clear the file

    # Process each line
    for line in lines:
        n, r, operation = line.split()
        n = int(n)
        r = int(r)

        # Perform the calculation and write the result back into the file
        if operation == 'C':
            result = nCr(n, r)
            file.write(f'{n} {r} C result of {n}C{r} is {result}\n')
        else:  # operation == 'L'
            result = lcm(n, r)
            file.write(f'{n} {r} L result of LCM({n}, {r}) is {result}\n')


#ques 2
# Open the file
with open('Assign5_2.txt', 'r+') as file:
    # Read the list and dictionary from the file
    my_list = [5, 2, 'test', 9, 7]
    my_dict = {"food": 5, "test": 12}

    # Go through each item in the list
    for i in range(len(my_list)):
        # If the item is a string and it's a key in the dictionary
        if type(my_list[i]) == str and my_list[i] in my_dict:
            # Replace the string with the value from the dictionary
            my_list[i] = my_dict[my_list[i]]

    # Clear the file and write the updated list and dictionary
    file.seek(0)
    file.truncate()
    file.write('list1 = ' + str(my_list) + '\n')
    file.write('dict1 = ' + str(my_dict) + '\n')


#ques 3
def display_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        short_words = [word for word in words if len(word) < 4]
        print(f"{len(short_words)} words are having less than 4 characters.")
        return short_words

def count_words_ending_with_e(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        words_ending_with_e = [word for word in words if word.endswith('e')]
        print(f"{len(words_ending_with_e)} words are ending with alphabet 'e'.")
        return words_ending_with_e

def mTOt(filename):
    with open(filename, 'r') as file:
        text = file.read()
    with open(filename, 'w') as file:
        file.write(text.replace('m', 't').replace('M', 't'))

# Test the functions
filename = 'story.txt'
display_words(filename)
count_words_ending_with_e(filename)
mTOt(filename)
