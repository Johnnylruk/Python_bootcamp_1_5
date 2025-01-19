print("Good Morning")

name = str(input("Good morning, what's your name? "))
print(f"It's nice to meet you {name}")

print("Once upon a time a princess lived in a farm with her parents.")
input("Press to continue... ")
print("Then a dragon from a short distance village woke up after several years into hibernating")
input("Press enter to continue...")

text = 'arara blue socorro car eve radar'


def Palindrome_check(text):
    
    text_split = text.split()
    palindrome = []

    for ch in text_split:
        reversed_text = ''
        for char in range(len(ch) -1 , -1, -1):
            reversed_text += ch[char]
            if reversed_text == ch:
                palindrome.append(reversed_text)
    print(palindrome)

Palindrome_check(text)

def factorial_number(number):
    factorial = 1

    for num in range(number, 0, -1):
        factorial *= num
    print(factorial)

factorial_number(6)