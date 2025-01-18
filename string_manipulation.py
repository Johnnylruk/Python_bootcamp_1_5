# name = str(input("Please type your name ")).strip()

# name_upper = name.upper()
# name_lower = name.lower()

# total_letters = name.replace(" ", "")

# name_split = name.split()

# print(f"The user full name with all upper case letters is {name_upper} ")
# print(f"The user full name with all lower case letters is {name_lower} ")
# # another way to do without spaces:
# print(f"The count of total letters is: {len(name)} and the letters without space is: {len(name) - name.count(' ')}")
# print(f"The count of total letters is: {len(name)} and the letters without space is: {len(total_letters)} ")
# print(f"The user first name is {name_split[0]} ")


# number = int(input("Type a positive number: "))

# while number < 0:
#     number = int(input("Type a positive number: "))

# unit = number // 1 % 10
# ten = number // 10 % 10
# hundred = number // 100 % 10
# thousand = number // 1000 % 10

# print(f"Analising number {number}")
# print(f"Number unidade: {int(unit)}")
# print(f"Number dezena: {int(ten)}")
# print(f"Number centena: {int(hundred)}")
# print(f"Number milhar: {int(thousand)}")

# text = str(input("Please type a text ")).strip().upper()

# print(f"The letter A displays {text.count('A')} times.")
# print(f"The first letter A displays at {text.find('A')+ 1} position.")
# print(f"The last letter A displays at {text.rfind('A')+ 1} position.")

# name = str(input("What's your name? ")).strip().split()

# print(f"Nice to meet you")
# print(f"Your first name is {name[0]}")
# print(f"Your first name is {name[-1]}")


# import time

# for num in range(10, 0, -1):
#     time.sleep(1)
#     print(num)
# print("Happy New Year!!!!!!!!!!!!!!!!!!!!")

# for num in range(1,50):
#     if num % 2 == 0:
#         print(num)

# sum = 0
# for num in range(1,500):
#     if  num % 2 == 1 and num % 3 == 0:
#         sum += num
# print(sum)

# number = int(input("Please pick a number: "))

# for num in range(1, 11):
#     total = num * number
#     print(f"{num} * {number} = {total}")

# sum = 0
# for num in range(1,7):
#     number = int(input("Type a positive number: "))
#     if number > 0:
#         if number % 2 == 0:
#             sum += number
#     elif number <= 0:
#         print("Invalid number, program will not count")
# print(sum)

# termo = int(input("Please insert number for termo "))
# razao = int(input("Please insert number for razao "))

# for num in range(termo, razao * 10,razao):
#     print(num)

# text = str(input('Write a text to check if is a Palindrome: ')).strip().lower()

# text = text.replace("-", "")
# text = text.replace(',' , '').split()
# text_join = ''.join(text)

# reversed_text = ''

# for char in range(len(text) -1, -1, -1):
#     reversed_text += text[char]
# if text == reversed_text:
#     print('The text is a Palindrome')
# else:
#     print('The text it is not a Palindrome')

# over_18 = 0
# under_18 = 0

# for date in range(1,8):    
#     dob = int(input("Please, inform your DOB "))

#     age = 2025 - dob

#     if age >= 18:
#         over_18 += 1
#     else:
#         under_18 += 1
# print(f"People equal or over 18 {over_18}, people under 18 {under_18}")


# high_weight = 0
# low_weight = 0

# for time in range(1,6):
#     weight = int(input('say weight '))
    
#     if weight > high_weight:
#         high_weight = weight
#     elif weight < low_weight:
#         low_weight = weight
#     elif low_weight == 0:
#         low_weight = weight
# print(f"Highest weight: {high_weight}")
# print(f"Lowest weight:{low_weight} ")


# mean = 0
# older = 0
# who = ''
# count_woman = 0

# for time in range(1,5):
#     name = str(input("Please type your name ")).strip()
#     age = int(input("Please type your age "))
#     gender = str(input("Please type your gender "))

#     if age > older and gender.lower() == 'male':
#         older = age
#         who = name
#     if gender.lower() == 'female' and age < 20:
#         count_woman += 1
#     mean += age / 4

# print(f"The mean of the group is {int(mean)}.")
# print(f"The oldest man is:  {who} and he is {older} years old. ")
# print(f"There is/are {count_woman} in this group who is under 20")
    



## DESAFIOS para assistir
# 55, 52, 50, 49,

# number = int(input('Type a number '))

# for num in range(1, number + 1):
#     if number % num == 0:
#         print('\033[34m', end='')
#     else:
#         print('\033[33m', end='')
#     print(num, end='')

# Reversing String
# data = 'mystring'

# for char in range(len(data) - 1, -1, -1):
#     print(data[char])

# data = 'myString'

# reversed_string = ''

# for char in range(len(data) - 1, -1, -1):
#     reversed_string += data[char]
# print(reversed_string)

