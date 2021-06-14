import random
import game

game_title = """    ██   ██ ██    ██ ███    ██ ████████ ███████ ██████  
    ██   ██ ██    ██ ████   ██    ██    ██      ██   ██ 
    ███████ ██    ██ ██ ██  ██    ██    █████   ██████  
    ██   ██ ██    ██ ██  ██ ██    ██    ██      ██   ██ 
    ██   ██  ██████  ██   ████    ██    ███████ ██   ██ 
    
    Autor: Jose Francisco Sandoval\n"""

print(game_title)

name = input("Ingresar apodo: ")

number = random.randint(0,100)

print(f"\nBienvenido {name} al examen de cazador. Este evento muy importante se realiza cada año, siendo miles los participantes que se inscriben para intentar conseguir su licencia de cazador.")
print(f"Tu numero de aspirante es el {number}")

g = game.Game(name, number)