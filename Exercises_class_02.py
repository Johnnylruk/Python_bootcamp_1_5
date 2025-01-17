
'''Create a program that checks if a word or phrase is a palindrome (reads the same backward as forward, ignoring spaces and punctuation). Use try-except to ensure the input is a string. Tip: Use the isinstance() function to check the type of the input.'''


# try:
#   celsius = float(input("Type a celsius temperature: "))
#   fahrenheit = (celsius * 1.8) + 32
#   print(f"The converted Celsius to Fahrenheit is : {fahrenheit}")
# except ValueError:
#   print("You do not input a valid temperature")

'''Develop a simple calculator that accepts two numeric inputs and an operator (+, -, , /) from the user. Use try-except to handle division by zero and non-numeric inputs. Use if-elif-else to perform the mathematical operation based on the provided operator. Print the result or an appropriate error message.'''


# try:
#   number_one = int(input("Please type the first number: "))
#   number_two = int(input("Please type the second number: "))
#   operator = input("Please type an operator '+', '-', '/' or '*' ")

#   if operator == '+':
#     result = number_one + number_two
#     print(f"The results of your sum operation is: {result}")
#   elif operator == '-':
#     result = number_one - number_two
#     print(f"The results of your minus operation is: {result}")
#   elif operator == '*':
#     result = number_one * number_two
#     print(f"The results of your multiplication operation is: {result}")
#   elif operator == '/':
#     result = number_one / number_two
#     print(f"The results of your division operation is: {int(result)}")
#   else:
#     print("Please, select a valid operator")

# except ZeroDivisionError:
#   print("You tried to divide 0 by 0.")
# except TypeError:
#   print("You have input the wrong type.")
# except ValueError:
#   print("You have input the wrong value.")

'''Write a program that prompts the user to enter a number. Use try-except to ensure the input is numeric and use if-elif-else to classify the number as "positive," "negative," or "zero." Additionally, identify if the number is "even" or "odd."'''

# try:
#   number = int(input("Please type a number: "))

#   if number > 0:
#     if number % 2 == 0:
#       print("You have entered a even positive number")
#     else:
#       print("You have entered a odd positive number")
#   elif number < 0:
#     print("You have entered a negative number")
#   else:
#     print("You have entered zero")
# except ValueError:
#   print("Please input a number.")

