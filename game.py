from random import choice
import random
from play import Lizard, Paper, Result, Rock, Scissors, Spock

def run_game():
    """ Inicia el juego """
    display_game()
    user_play = get_user_play()
    comp_play = random_play()
    display_match(user_play, comp_play)
    winner = get_winner(user_play, comp_play)
    if winner == None: # empate
        display_tie(user_play, comp_play)
    else:
        display_victory(winner)
    while another_match():
        run_game()
        break
    
def display_match(play1, play2):
    print(f'{play1.description()} vs {play2.description()}   \n\n\t🤼 FIGHT!\n')
    
def display_game():
    """ Muestra el nombre del juego """
    print('\n\n\t\tRock Paper Scissors Lizard Spock\n\n')

def get_user_play():
    """ Le pregunta al usuario qué quiere jugar y lo devuelve """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    elif res == 3:
        return Scissors()
    elif res == 4:
        return Lizard()
    else:
        return Spock()

def get_user_response():
    """
    Presenta un menu de opciones y pide que seleccione una.
    Devuelve una cadena que indica lo que ha elegido
    """
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock 🪨")
        print("2. Paper 🧻")
        print("3. Scissors ✂️")
        print("4. Lizard 🦎")
        print("5. Spock 🖖")
    
        raw = input("Enter 1, 2, 3, 4 or 5: \n")

        raw = raw.strip()
        if raw == "1":
            response = 1
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3": 
            response = 3
            break
        elif raw == "4": 
            response = 4
            break
        elif raw == "5": 
            response = 5
            break
        else:
            continue  
    return response

def random_play():
    """ Selecciona una jugada al azar para competir con el usuario """
    return choice([Paper(), Rock(), Scissors(), Lizard(), Spock()])

def get_winner(play1, play2):
    """ Obtiene el ganador o None si hay empate """
    winner = None
    result = play1.compare(play2)
    if result == Result.WINS:
        winner = play1  
    elif result == Result.LOSES:
        winner = play2
    else:
        winner = None
    return winner


def display_tie(play1, play2):
    """ Imprime que ha habido un empate """
    print(f'Tie between {play1.description()} & {play2.description()}')

def display_victory(winner):
    """ Muestra que winner ha ganado """
    print(f'Has won {winner.description()} ! ! !')

def another_match():
    while True:
        play_again = input("\nDo you want to play again (y/n)? ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            goodbye = ["¿Eres un gallina, McFly?", "¡Cobarde!", "Bye, bye perdedor"]
            print(random.choice(goodbye))
            return False
        else:
            print("Error. You must enter 'y' or 'n'.")
            continue

if __name__ == '__main__':
    run_game()
