from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()

    if player == ai:
        result = 'Empate!'
    else:
        if player == 'piedra':
            if ai == 'papel':
                result = 'Perdiste!'
            else:
                result = 'Ganaste!'
        
        if player == 'papel':
            if ai == 'tijeras':
                result = 'Perdiste!'
            else:
                result = 'Ganaste!'
        
        if player == 'tijeras':
            if ai == 'piedra':
                result = 'Perdiste!'
            else:
                result = 'Ganaste!'

    return result

# Entry Point
def Game():
    player = input('Player-1 elige Piedra, Papel o Tijeras: ')
    
    ai = options[randint(0,2)]
    
    winner = quienGana(player, ai)

    print(winner)
