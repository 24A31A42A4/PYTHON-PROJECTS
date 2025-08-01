import random
letters = ['a', 'b', 'c', 'd', 'e', 'f','A','B','C','D','E','F']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', ':', '?', '`', '~']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
l=str()
s=str()
n=str()
print("Welcome to the Pasword Generator:")
input_letters=int(input("How many Letters in password : "))
input_symbols=int(input("How many Symbols in password : "))
input_numbers=int(input("How many Numbers in password : "))
fpassword=[]
for i in range(input_letters):
    random_letters=random.randint(0,len(letters)-1)
    fpassword.append(letters[random_letters])
for i in range(input_symbols):
    random_symbols=random.randint(0,len(symbols)-1)
    fpassword.append(symbols[random_symbols])
for i in range(input_numbers):
    random_numbers=random.randint(0,len(numbers)-1)
    fpassword.append(numbers[random_numbers])

random.shuffle(fpassword)
password = ''.join(fpassword)
print(f" 🔒 The password is {password}")
print("Dont share it to any one 🙈 ")
