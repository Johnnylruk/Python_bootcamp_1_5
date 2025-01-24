# list_of_numbers = []
# highest_number = 0
# lowest_number = 0
# pos_high = 0
# pos_low = 0

# for num in range(0, 5):
#   list_of_numbers.append(int(input("Type a number: ")))
#   for pos , number in enumerate(list_of_numbers):
#     if highest_number == 0:
#       highest_number = number
#       pos_high = pos
#       lowest_number = number
#       pos_low = pos
#     elif number > highest_number:
#       highest_number = number
#       pos_high = pos
#     elif number < lowest_number:
#       lowest_number = number
#       pos_low = pos
# print(list_of_numbers)
# print(f'The Highest number is: {highest_number} at position {pos_high} and the lowest number is: {lowest_number} at position {pos_low}')


# list_of_numbers = []
# answer = 'Yes'.upper()

# while answer == 'Yes'.upper():
#   number = int(input("Type a number: "))
#   if number in list_of_numbers:
#     list_of_numbers.remove(number)
#     list_of_numbers.append(number)
#     print("Duplicated value, I will not add. ")
#   else:
#       list_of_numbers.append(number)
#   list_of_numbers.sort()
#   question = str(input("Do you want to continue? Yes or No? ")).upper()
#   while question != 'Yes'.upper() and question != 'No'.upper():
#      question = str(input("Do you want to continue? Yes or No? ")).upper()
#   if question == "No".upper():
#     answer = question
# print(list_of_numbers)


# list_of_numbers = []
# number_position = 0

# for num in range(1,6):
#   number = int(input("Please, type a number: "))
#   if num == 1 or number > list_of_numbers[len(list_of_numbers) - 1]:
#       list_of_numbers.append(number)
#       print("Number added at the end of the list.")
#   else:
#      while number_position < len(list_of_numbers):
#         if number <= list_of_numbers[number_position]:
#            list_of_numbers.insert(number_position,number)
#            break
#         number_position += 1
# print(list_of_numbers)


# list_of_numbers = list()
# five_position = 0

# while True:
#   number = int(input("Please type a number "))
#   list_of_numbers.append(number)
#   answer = input("Do you wish to continue? Y/N ").upper()
#   if answer == 'N':
#     print(f"You have typed {len(list_of_numbers)} numbers.")
#     list_of_numbers.sort(reverse=True)
#     print(f"This is your list of numbers in decrescent order {list_of_numbers}")
#     if 5 not in list_of_numbers:
#       print("You do not have number 5 in your list.")
#     for pos, num in enumerate(list_of_numbers):
#       if num == 5:
#         five_position = pos 
#         print(f"You have number 5 as position {pos} of your list.")
#     break
  


# list_of_numbers = list()
# list_of_even_numbers = list()
# list_of_odd_numbers = list()

# while True:
#   number = int(input("Please, type a number: "))
#   list_of_numbers.append(number)
#   if number % 2 == 0:
#     list_of_even_numbers.append(number)
#   else:
#     list_of_odd_numbers.append(number)
#   answer = input("Do you wish to continue?... Y/N ").upper()
#   if answer == 'N':
#     list_of_even_numbers.sort()
#     list_of_numbers.sort()
#     list_of_odd_numbers.sort()
#     print(f"Your numbers list is {list_of_numbers}")
#     print(f"Your odd numbers are {list_of_odd_numbers}")
#     print(f"Your even numbers are {list_of_even_numbers}")
#     break

# lb_count = 0
# rb_count = 0
# expression = list(input("Gimme math expression "))

# for ch in expression:
#     if ch == "(":
#         left_brackets = ch
#         lb_count += 1
#     elif ch == ")":
#         right_brackets = ch
#         rb_count += 1

# if rb_count == lb_count:
#     print("Valid Expression")
# else:
#     print("Not Valid Expression")

# people = list()
# data = list()

# for d in range(3):
#     data.append(str(input("Name: ")))
#     data.append(int(input("Age: ")))
#     people.append(data[:])
#     data.clear()

# for person in people:
#     if person[1] > 18:
#         print(person[0])

# people = list()
# data = list()
# lower_weight = 0
# higher_weight = 0
# who_higher, who_lower = '',''
# while True:
#     data.append(str(input("Name: ")))
#     data.append(float(input("Weight: ")))
#     people.append(data[:])
#     data.clear()
#     answer = str(input("Do you like to continue? Y/N "))
#     if answer in 'Nn':
#       print(f"You have registered {len(people)} people.")
#       for pos, weight in enumerate(people):
#           if pos == 0:
#              lower_weight = weight[1]
#              higher_weight = weight[1]
#           else:
#             if weight[1] > higher_weight:
#                 higher_weight = weight[1]
#                 who_higher = weight[0]
#             elif weight[1] < lower_weight:
#                lower_weight = weight[1]
#                who_lower += weight[0]
#       print(f"The highest weight is: {higher_weight} that belongs to {who_higher}")
#       print(f"The lowest weight is: {lower_weight} that belongs to {who_lower}")
#       break

# list_of_numbers = [[],[]]
# print(list_of_numbers)
# for num in range(7):
#     number = int(input("Type a number: "))
#     if number % 2 == 0:
#         list_of_numbers[1].append(number)
#     else:
#         list_of_numbers[0].append(number)
# list_of_numbers.sort()
# print(f"The odd numbers typed is/are: {list_of_numbers[0]}")
# print(f"The even numbers typed is/are: {list_of_numbers[1]}")

# matrix = []
# data = []
# sum_even = 0
# highest_sec_col_value = 0
# for n in range(0,3):
#     number = int(input(f"Type number for [0:{n}]: "))
#     if number % 2 == 0:
#       sum_even += number
#     data.append(number)
# matrix.append(data[:])
# data.clear()
# for n in range(0,3):
#     number = int(input(f"Type number for [1:{n}]: "))
#     if number % 2 == 0:
#       sum_even += number
#     if n == 0:
#        highest_sec_col_value = number
#     elif highest_sec_col_value < number:
#        highest_sec_col_value = number
#     data.append(number)
# matrix.append(data[:])
# data.clear()
# for n in range(0,3):
#     number = int(input(f"Type number for [2:{n}]: "))
#     if number % 2 == 0:
#       sum_even += number
#     data.append(number)
# matrix.append(data[:])
# data.clear()
# third_col_sum = matrix[0][2] + matrix[1][2] + matrix[2][2]

# print(f"[ {matrix[0][0]} ][ {matrix[0][1]} ][ {matrix[0][2]} ]")
# print(f"[ {matrix[1][0]} ][ {matrix[1][1]} ][ {matrix[1][2]} ]")
# print(f"[ {matrix[2][0]} ][ {matrix[2][1]} ][ {matrix[2][2]} ]")
# print(f"The sum of even numbers is: {sum_even}")
# print(f"The sum of third column is: {third_col_sum}")
# print(f"The highest second column value is: {highest_sec_col_value}")

import random as rd

loterry_numbers = []
list_of_numbers = []
for num in range(60):
    loterry_numbers.append(num)
answer = int(input("How many games you want to generate? "))

for num in range(answer * 6):
    random = rd.choice(loterry_numbers)
    list_of_numbers.append(random)
print(list_of_numbers)
    