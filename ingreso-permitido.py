
#1. Solicitar al usuario que ingrese la edad del cliente
edad=int(input('Porfavor, ingresa tu edad: '))


#2. Verificar si la edad ingresada cumple con el requisito para ingresar
permitido=True

if edad >= 18:
    permitido=True
else:
    permitido=False


#3. Mostrar al usuario si el cliente puede o no ingresar

if permitido:
    print('Puede ingresar a la discoteca')
else:
    print('Lo sentimos, no puede ingresar a la discoteca')