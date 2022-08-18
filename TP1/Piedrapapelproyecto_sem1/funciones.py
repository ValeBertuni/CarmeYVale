import random

def combate(p_armajugador):
    ops=['piedra','papel','tijera']
    armapc=random.choice(ops)
    if p_armajugador==armapc:
        print("Su arma:", p_armajugador) 
        print("Arma oponente:",armapc)
        print("Resultado: empate")
    elif p_armajugador=='tijera' and armapc=='papel':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has ganado")
    elif p_armajugador=='papel' and armapc=='piedra':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has ganado")
    elif p_armajugador=='piedra' and armapc=='tijera':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has ganado")
        
    elif armapc=='tijera' and p_armajugador=='papel':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has perdido")
    elif armapc=='papel' and p_armajugador=='piedra':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has perdido")
    elif armapc=='piedra' and p_armajugador=='tijera':
        print("Su arma:", p_armajugador)
        print("Arma oponente:",armapc)
        print("Resultado: has perdido")
        
    return("Fin de la partida")
