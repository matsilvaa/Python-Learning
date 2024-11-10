# https://www.w3resource.com/python-exercises/string/

# 1. Write a Python program to calculate the length of a string.

text = input("Write a random text:\n")
print(len(text))    # Result: text len


# 2. Write a Python program to count the number of characters (character frequency) in a string. 

def char_frequency(str1):
    dict = {}  
    for n in str1:
        if n in dict:  
            dict[n] += 1
        else: 
            dict[n] = 1

    return dict
print(char_frequency("google.com")) #Result: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# 3 .Write a Python program to get a string made of the first 2 and last 2 characters of a given string.

def last_letters(str1):


    first_char = str1[0]
    second_char = str1[1]

    penultimate_char = str1[-2]
    last_char = str1[-1]

    indices = (f"{first_char}, {second_char}, {penultimate_char}, {last_char}")
    return indices

print(last_letters("pindamonhongaba"))

# 4 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_char(str1):
    char = str1[0]

    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

print(change_char('Aranigaldoarasta'))

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap_string(str1, str2):
    char1 = str1[0]
    char2 = str2[0]

    swap1 = char2 + str1[1:]
    swap2 = char1 + str2[1:]

    result = swap1 + swap2
    return result

print(swap_string("peixe", "sapato"), sep=" ")

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def add_string(str1):
    tamanho = len(str1)

    if tamanho > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    
    return str1

print(add_string('ab'))    
print(add_string('abc'))   
print(add_string('string'))

# 7. Find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

# Define a function named not_poor that takes one argument, 'str1'.
def not_poor(str1):
    # Find the index of the substring 'not' in the input string 'str1' and store it in 'snot'.
    snot = str1.find('not')
    
    # Find the index of the substring 'poor' in the input string 'str1' and store it in 'spoor'.
    spoor = str1.find('poor')

    # Check if 'poor' is found after 'not', and both 'not' and 'poor' are present in the string.
    if spoor > snot and snot > 0 and spoor > 0:
        # Replace the substring from 'snot' to 'spoor+4' (inclusive) with 'good'.
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        # If the conditions are not met, return the original 'str1'.
        return str1

print(not_poor())