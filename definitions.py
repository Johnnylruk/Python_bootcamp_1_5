# def list_sum(num: list) -> list:
#   return sum(num)

# def check_prime_number(number: int) -> bool:
#   if number <= 1: return False
  
#   for num in range(2,number):
#     if number % num == 0:
#       return False
#     return True
  
# print(check_prime_number(2))

# def making_reversed_string(text: str) -> str:

#   reversed_string = text[::-1] 
#   return reversed_string

# print(making_reversed_string('testing'))

# def incrementing_sum(list_num: list, num: int) -> int:
  
#   list_of_evens = [number + num for number in list_num if (number + num) % 2 == 0]
#   return list_of_evens

students = {
    'Name' : 'Johnny',
    'Age' : 55,
    'University' : 'MIT',
    'Period': 'Morning'
}

def getting_dict_to_list_of_keys(dict: dict) -> list:
  
  list_of_keys = [key for key in dict.keys()]
  list_of_keys.sort()
  return list_of_keys

print(getting_dict_to_list_of_keys(students))

