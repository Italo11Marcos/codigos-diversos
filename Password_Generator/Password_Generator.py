import random

password = []

pw = ''

#Add numbers 0-9 in password
for i in range(10):
    password.append(str(i))

#Convert and add the characters in upper in password
for i in range(65,91):
    password.append(chr(i))

#Convert and add the characters in lower in password
for i in range(97,123):
    password.append(chr(i))

tam = int(input("Enter with lenght to password: "))

i = 0
#While true, add a random character in string pw
while True:
    i += 1
    if i == tam+1:
        break
    x = random.choice(password)
    pw += x

print(pw)
