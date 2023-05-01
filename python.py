def word(name):
    count=0
    vowels='a','e','i','o','u'
    for i in name:
        for b in vowels:
            if(i==b):
                count+=1
    return count
print(word("Regina"))


# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition(a,b):
    add=a+b  
    return add
print(addition(10,2))  

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_string(name):
    reverse=name[::-1]
    return reverse
print(reverse_string("Regina"))

# Write a Python function that takes a list of integers as input and returns the
#  sum of all the integers in the list.
def add_numbers(numbers):
    sum=0  
    for i in numbers:
     sum+=i
    return sum
print(add_numbers([2,3,4,5,6,7])) 

# Write a Python function that takes a list of integers as input and returns
#  a new list with all the even numbers removed.
def remove_even_numbers(nums):
    empty=[]
    for i in nums:
        if i%2!=0:
            return empty.push(i)
print(remove_even_numbers([1,2,3,4,5,6,7,8,9,10]))


# Write a Python function that takes a list of integers as input and returns the
#  highest value in the list.
def largest_num(numbers):
    highest=numbers[0]
    for i in numbers:
         if i>highest:
           highest=i
    return highest
output=largest_num([1,2,3,4,5,6,7])
print(output)


    
# # Write a Python function that takes a list of strings as input and returns a new 
# # list with all the strings capitalized.
def caps(name):
    return  name.capitalize()
print(caps(["Regina","Chege","Wairimu"]))

             











        