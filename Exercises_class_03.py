'''Exercise 1: Data Quality Check You are analyzing a sales dataset and need to ensure that all records have positive values for quantity and price. Write a program that checks these fields and prints "Valid data" if both are positive or "Invalid data" otherwise.'''

# try:
#   quantity = int(input("Please, input the quantity "))
#   price = float(input("Please, input price "))

#   if quantity > 0 and price > 0:
#     print('Valid data')
#   else:
#     print('Invalid data')
# except ValueError:
#   print("Please, insert correct value")



'''Exercise 3: Word Count in Texts Objective: Given a text, count how many times each unique word appears in it.'''

# text = "My car is black but my wife's car is blue"

# text_to_list = text.split()

# count = 1
# text_count = {}

# for phrase in text_to_list:
#   if phrase in text_count:
#     text_count[phrase] = count + 1
#   else:
#     text_count[phrase] = count
  
# print(text_count)
  

'''Exercise 4: Log Filtering by Severity You are analyzing application logs and need to filter messages with severity 'ERROR'.
Given a log record in dictionary format like 
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failure'}, write a program that prints the message if the severity is 'ERROR'.'''

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failure'}
  
# for text, value in log.items():
#   if value == 'ERROR':
#     print(f"The ERROR message is: {log['message']}")

### Exercício 5: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# users = [
#     {"user_name": "alice_wonder", "age": 17, "email": "alice@example.com"},
#     {"user_name": "bob_builder", "age": 34, "email": "bob@example.com"},
#     {"user_name": "charlie_brown", "age": 22, "email": "charlie@example.com"},
#     {"user_name": "diana_prince", "age": 30, "email": "dianaexample.com"},
#     {"user_name": "edward_snow", "age": 66, "email": "edward@example.com"}
# ]

# for user in users:
#   if user["age"] >= 18 and user['age'] <= 65:
#     if not '@' in user['email']:
#       print(f'The user: {user['user_name']} has valid data.')
#     else:
#       print(f'The user: {user["user_name"]} has an invalid email')
  
#   print(f'The user: {user['user_name']} is not in the age range between')
        
### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# users = [
#     {"user_name": "alice_wonder", "age": 28, "email": "alice@example.com"},
#     {"user_name": "bob_builder", "age": 34, "email": "bob@example.com"},
#     {"user_name": "charlie_brown", "age": None, "email": "charlie@example.com"},
#     {"user_name": "diana_prince", "age": 30, "email": None},  
#     {"user_name": "edward_snow", "age": 26, "email": "edward@example.com"}
# ]

# for user in users:
#   if None in user.values():
#     print(f'This user {user['user_name']} has a missing value')



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# list_of_numbers = range(1,100)

# for number in list_of_numbers:
#   if number % 2 == 0:
#     print(number)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

sales_records = [
    {"register_of_sales": 1, "value_of_sales": 150.00, "category": "Electronics"},
    {"register_of_sales": 2, "value_of_sales": 85.50, "category": "Books"},
    {"register_of_sales": 3, "value_of_sales": 200.00, "category": "Furniture"},
    {"register_of_sales": 4, "value_of_sales": 45.75, "category": "Clothing"},
    {"register_of_sales": 5, "value_of_sales": 120.00, "category": "Toys"},
    {"register_of_sales": 6, "value_of_sales": 300.00, "category": "Electronics"},
    {"register_of_sales": 7, "value_of_sales": 60.00, "category": "Books"},
    {"register_of_sales": 8, "value_of_sales": 250.00, "category": "Furniture"},
    {"register_of_sales": 9, "value_of_sales": 75.00, "category": "Clothing"},
    {"register_of_sales": 10, "value_of_sales": 90.00, "category": "Toys"}
]

result_per_category = {}


for text in len(sales_records):
  print(text)
