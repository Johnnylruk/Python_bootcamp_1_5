# nome_valido: bool = False
# salario_valido: bool = False
# bonus_valido: bool = False

# while not nome_valido:
#     try:
#         nome: str = input("Digite seu nome: ")

#         # Verifica se o nome está vazio
#         if len(nome) == 0:
#             raise ValueError("O nome não pode estar vazio.")
#         # Verifica se há números no nome
#         elif any(char.isdigit() for char in nome):
#             raise ValueError("O nome não deve conter números.")
#         else:
#             print("Nome válido:", nome)
#             nome_valido: bool = True
#     except ValueError as e:
#         print(e)

# # Solicita ao usuário que digite o valor do seu salário e converte para float

# try:
#     salario: float = float(input("Digite o valor do seu salário: "))
#     if salario < 0:
#         print("Por favor, digite um valor positivo para o salário.")
# except ValueError:
#     print("Entrada inválida para o salário. Por favor, digite um número.")
#     exit()

# # Solicita ao usuário que digite o valor do bônus recebido e converte para float
# try:
#     bonus: float = float(input("Digite o valor do bônus recebido: "))
#     if bonus < 0:
#         print("Por favor, digite um valor positivo para o bônus.")
# except ValueError:
#     print("Entrada inválida para o bônus. Por favor, digite um número.")
#     exit()

# bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# # Imprime as informações para o usuário
# print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# square = [num * num for num in range(1,11)]
# print(square)

# list = ["Python", "Java", "C++", "JavaScript"]
# list.remove('C++')
# list.append('Ruby')
# print(list)

# book = {
#     'Book_Name': 'Star Wars',
#     'Author': 'George Lucas',
#     'Year': 1980
# }

# for key, value in book.items():
#   print(f"{key}: {value}")

# def counting_char(char):
#   count = {}

#   for c in char:
#     count[c] = count.get(c, 0) + 1
#   return count

# print(counting_char("Data Engineer"))

# fruits = ['Apple', 'Banana', 'Cherry']
# prices = {
#       'Apple': 0.45,
#       'Banana': 0.30,
#       'Cherry': 0.65
# }

# total_prices = sum(prices[price] for price in prices)
# print(total_prices)

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# distinct_emails = []

# for email in emails:
#   if email not in distinct_emails:
#     distinct_emails.append(email)
# distinct_emails.sort()

# # distinct_emails = list(set(emails))

# print(distinct_emails)

# ages = [11,18,22,35,17]

# filtered_ages = [age for age in ages if age >= 18]
# print(filtered_ages)

# import operator

# people = [
#     {"name": "Bob", "idade": 30},
#     {"name": "Alice", "idade": 25},
#     {"name": "Carol", "idade": 20}
# ]

# #people = sorted(people, key=operator.itemgetter('name'))
# people.sort(key=lambda person: person["name"])

# print(people)

# numbers = [num for num in range(1,50,4)]
# count = 0
# for m in numbers:
#   count += m
# print(numbers)
# mean = count / len(numbers)

# print(int(mean))

# numbers = [num for num in range(1,50,4)]

# mean = sum(numbers) / len(numbers)
# print(mean)

# numbers = [num for num in range(1,50,3)]
# odd = [num for num in numbers if num % 2 != 0]
# even = [num for num in numbers if num % 2 == 0]

# print(f'Evens: {even}')
# print(f'Odds: {odd}')


# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# list_dictionarioes = [dicionario1, dicionario2]

# dict_list = {**dicionario1, **dicionario2}

# print(list_dictionarioes)
# print(dict_list)

# stock = {"Keyboard": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# filtering_stock = {product: price for product, price in stock.items() if price > 0}
# print(filtering_stock)

# dictionaries = {"a": 1, "b": 2, "c": 3}

# keys = list(dictionaries.keys())
# values = list(dictionaries.values())

# print(f'Keys: {keys}')
# print(f'Values: {values}')


def counting_freq(char):
  count_freq = {}

  for c in char:
    if c in count_freq:
      count_freq[c] += 1
    else:
      count_freq[c] = 1
  return count_freq

print(counting_freq("Data Engineer"))