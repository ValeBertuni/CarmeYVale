import funciones

comunespiepap=['p']
comunespietij=['i', 'ra']
comunesatres=['a','e']
repeticiones=['p','i','a','e','ra'] #if in rep: volver a ingresar

print("Bienvenido a al juego de piedra papel o tijera")
arma=input("Ingrese cualquier letra jugar, ingrese 'cerrar' para finalizar el juego: ")
while arma != 'cerrar' and arma !='CERRAR':
    arma=input("Elija un arma o ingrese 'cerrar' para finalizar el juego: ")
    arma=arma.lower()
    if arma=='p' or arma=='i' or arma=='ra'or arma=='a'or arma=='e' :
        print("Respuesta insuficiente, podria ser mas de un arma, vuelva a elegir")
    if arma in 'piedra' and arma!='p' and arma!='i' and arma!='ra' and arma!='a'and arma!='e':
        print("Ha elegido piedra")
        arma='piedra'
        print(funciones.combate(arma))
    if arma in 'papel' and arma!='p' and arma!='a' and arma!='e':
        print("Ha elegido papel")
        arma='papel'
        print(funciones.combate(arma))
    if arma in 'tijera' and arma!='i' and arma!='ra' and arma!='a'and arma!='e':
        print("Ha elegido tijera")
        arma='tijera'
        print(funciones.combate(arma))