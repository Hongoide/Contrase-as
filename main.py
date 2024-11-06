import random as r
import string as s
elements = s.ascii_letters + s.digits + s.punctuation
lenght = int(input("Introduce la longuitud de la contraseña: "))

password = ""
for i in range(lenght):
    password += r.choice(elements)
print(password) 