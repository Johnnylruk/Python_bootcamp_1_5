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


list_of_numbers = []
number_position = 0

for num in range(1,6):
  number = int(input("Please, type a number: "))
  if num == 1 or number > list_of_numbers[len(list_of_numbers) - 1]:
      list_of_numbers.append(number)
      print("Number added at the end of the list.")
  else:
     while number_position < len(list_of_numbers):
        if number <= list_of_numbers[number_position]:
           list_of_numbers.insert(number_position,number)
           break
        number_position += 1
print(list_of_numbers)


