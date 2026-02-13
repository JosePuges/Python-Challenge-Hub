#Escribir un programa que pida al usuario dos números enteros y 
# muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
# donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = (input("Primer numero entero: "))
m = (input("Segundo numero entero: "))

print(n + " entre " + m + " da un cociente de " + str(int(n) // int(m)) + " y un resto de " + str(int(n) % int(m)))