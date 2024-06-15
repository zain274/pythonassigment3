
# 1.#  output the numbers from 1 to 10 using range function and for loop
# output should be like
# solution
# for i in range(1,11):
#     print(i)

# 2.output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc
# solution
# for i in range(35,51):
#     print(i)

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc
# solution
# for i in range(-15,-26,-1):
#     print(i)

# 4. output the numbers from 5 to -10 using range function and for loop/
# output should be like
# 5
# 4
# 3
# # etc
# solution
# for i in range(5,-11,-1):
#     print(i)

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc
# solution
# for i in range(0,51,3):
#     print(i)


# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc
# solution
# for i in range(1,11):
#     print("2 X",i,"=",2*i)

# Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

# solution
# numbers =[3,5,2,1,4]
# total_sum = 0
# for number in numbers:
#     total_sum += number

# print(total_sum)


# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

# solution

# numbers=[3,5,2,1,4]
# largest_number = numbers[0]
# for number in numbers:
#     if number > largest_number:
#         largest_number=number
#         print(largest_number)

# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]

# solution
# number=[10, 20, 30, 40, 50]
# total_sum=sum(number)
# print("the sum of all elements in a given list",total_sum)


# Exercise 2:Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]
# solution
# numbers=[12,7,9,24, 18, 5, 3, 20]
# even_num=0
# odd_num=0
# for i in numbers:
#     if i % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1

# # Print the results
# print("Number of even numbers in the list:", even_num)
# print("Number of odd numbers in the list:", odd_num)


#  Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

# solution
# even_numbers = [num for num in range(1, 21) if num % 2 == 0]

# print("List of even numbers from 1 to 20:", even_numbers)
    
# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry"
# solution
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index} Element: {fruit}")


# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = set(list1).intersection(set(list2))

# print("Common elements between the two lists:", list(common_elements))


# Find the Length of Each String in a List
# Objective: Write a Python program that finds and prints the length of each string in a given list.
# Example list
# strings = ["apple", "banana", "cherry", "date"]

# strings=["apple", "banana", "cherry", "date"]
# for string in strings:
#     print(f"lenght of '{string}' : {len(string)}")