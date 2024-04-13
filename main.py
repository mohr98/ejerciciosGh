print ("Bienvenido al mundo de la programacion")
nom = input("Para empezar, ingresa tu nombre")
print (f"Bienvenido {nom}")

#ejercicio 3

print("ingrese un valor para 'x' y podrás resolver la siguiente ecuacion")
x = int(input("(x^2+3x+1)/4"))
formula = (x**2+3*x+1)/4
print("el resultao de la operacion con el valor {x} es: {formula}", formula)

#ejercicio 4
nombre = input("ingrese su nombre\n")
rut = input("ingrese su rut con puntos y guion")
correo = input("ingrese su correo electronico")
telefono = input("ingrese su numero de telefonico")
dat = "datos personales"
print(dat.upper())
print("NOMBRE: \t", nombre.upper())
print("RUT: \t\t", rut)
print("CORREO: \t", correo.upper())
print("TELEFONO \t", telefono)