# 5. Establece dos valores, uno para usuario y otro para contraseña. Solicita por pantalla dos
# palabras para que el usuario introduzca el usuario y la contraseña, y 
# realiza la validación correspondiente.

user = "admin"
password = "123#"

userTry = input("Introduce el usuario: ")
passwordTry = input("Introduce la contraseña: ")

if userTry == user and password == passwordTry:
    print("Login correcto")
else:
    print("Usuario o contraseña incorrectos")