# 1. Write a Python program to get a single string from two given strings,
# separated by a space, and swap the first two characters of each string
def swap(fruits,type):
    fruit1=fruits[:2]+type[2:]
    type1=type[:2]+fruits[2:]
    return fruit1 , type1
print(swap("Mango","Tropical"))

# 2.  Write a Python function that takes a list of words and returns the 
# longest word and the length of the longest one
def longest_word(a,b):
    for i in b :
        for c in a:
            if(a.len()>=b.len()):
                return "longest"
print(longest_word("Regina","Chege"))

# Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5

def common_number():
    empty=[]
    list_a = [1, 2, 3, 4,] 
    list_b = [2, 3, 4, 5]
    new_list=list_a+list_b
    new_list=[n for n in new_list if n.find(2)]
    empty.append(n)
print(common_number())

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)
def divisible_by_2_and_9():
    divisible= [x for x in range(1, 1001) if any(x % number == 0 for number in range(2, 10))]
print(divisible_by_2_and_9())

#  Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
def remove_odd_numbers(num):
    count=0
    for x in num:
        if(x%2==0):
            return x
        else:
            return "none"
    count
num = [3,5,45,97,32,22,10,19,39,43]
print(remove_odd_numbers(num))

# 10. Write a Python function to remove all vowels in a string
def remove_vowels(word):
    empty=[]
    vowels="aeiouAEIOU"
    for x in word:
        if x in vowels:
            if x==vowels:
                return empty.push(x)
print(remove_vowels("Regina"))


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]



# 10. Write a Python function to remove all vowels in a string


# 6. Write a Python program to check whether all dictionaries in a list are empty or not


# 3. Write a Python program that accepts a comma-separated sequence of words as input
# and prints the distinct words in sorted form (alphanumerically).