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
# count = 0
# five_position = 0

# while True:
#   number = int(input("Please type a number "))
#   list_of_numbers.append(number)
#   count += 1
#   answer = input("Do you wish to continue? Y/N ").upper()
#   if answer == 'N':
#     print(f"You have typed {count} numbers.")
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

lb_count = 0
rb_count = 0
expression = list(input("Gimme math expression "))

for ch in expression:
    if ch == "(":
        left_brackets = ch
        lb_count += 1
    elif ch == ")":
        right_brackets = ch
        rb_count += 1

if rb_count == lb_count:
    print("Valid Expression")
else:
    print("Not Valid Expression")