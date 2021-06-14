#!/usr/bin/env python
import random

class Game:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def level1(self):
        print(
            "\nBienvenido a la etapa numero 1 del examen de cazador, para poder pasar a la siguiente etapa deberas de contestar correctamente la siguiente adivinanza\n")
        if self.number <= 33:
            print("Estás escapando de un laberinto, y hay tres puertas frente a ti. La puerta de la izquierda conduce a un infierno. La puerta en el centro te lleva a un asesino mortal. La puerta de la derecha te conduce a un león que no ha comido en tres meses. ¿Qué puerta eliges?")
            print("a) Puerta Izquierda")
            print("b) Puerta del Centro")
            print("c) Puerta derecha")
            res = input("Respuesta: ")
            if res.lower() != 'c':
                print("Haz respondido incorrectamente. No eres apto para continuar el examen de cazador")
        elif 33 < self.number <= 66:
            print("Ponedme de lado y seré todo. Cortadme a la mitad y seré nada. ¿Qué soy?")
            print("a) Una pera")
            print("b) Una navaja")
            print("c) El numero 8")
            res = input("Respuesta: ")
            if res.lower() != 'c':
                print("Haz respondido incorrectamente. No eres apto para continuar el examen de cazador")
        elif 66 < self.number <= 100:
            print("Un granjero tiene 10 conejos, 20 caballos y 40 cerdos. Si llamamos “caballos” a los “cerdos”, ¿cuántos caballos tendrá?")
            print("a) 20")
            print("b) 40")
            print("c) 60")
            res = input("Respuesta: ")
            if res.lower() != 'a':
                print("Haz respondido incorrectamente. No eres apto para continuar el examen de cazador")

        print("Haz respondido correctamente. Eres apto para continuar a la segunda etapa del examen de cazador")
        self.level_completed(1)

    def level2(self):
        print("\nHaz llegado a la segunda etapa del examen de cazador, a continuación tendras que jugar piedra papel o tijera con el cazador profesional Gon Freecs, para poder ganar deberas de ganar 1 juego y tienes solamente 3 oportunidades")
        val = 0
        while val < 3:
            print("\n!!!!PIEDRA PAPEL O TIJERA!!!!")
            print("1) Piedra")
            print("2) Papel")
            print("3) Tijera")
            op = int(input("Opcion: "))
            op_gon = random.randint(1, 3)

            if op == 1 and op_gon == 2:  # Piedra vs Papel
                print(f"{self.name}: Piedra")
                print("Gon: Papel")
                print("Papel envuelve a la piedra, Gon es el ganador")
                val += 1
            elif op == 1 and op_gon == 3:  # Piedra vs Tijera
                print(f"{self.name}: Piedra")
                print("Gon: Tijera")
                print(f"Piedra rompe tijera, {self.name} es el ganador")
                self.level_completed(2)
            elif op == 2 and op_gon == 1:  # Papel vs Piedra
                print(f"{self.name}: Papel")
                print("Gon: Piedra")
                print(f"Papel envuelve a la piedra, {self.name} es el ganador")
                self.level_completed(2)
            elif op == 2 and op_gon == 3:  # Papel vs Tijera
                print(f"{self.name}: Papel")
                print("Gon: Tijera")
                print("Tijera corta papel, Gon es el ganador")
                val += 1
            elif op == 3 and op_gon == 1:  # Tijera vs Piedra
                print(f"{self.name}: Tijera")
                print("Gon: Piedra")
                print("Piedra rompe tijera, Gon es el ganador")
                val += 1
            elif op == 3 and op_gon == 2:  # Tijera vs Papel
                print(f"{self.name}: Tijera")
                print("Gon: Papel")
                print(f"Tijera corta papel, {self.name} es el ganador")
                self.level_completed(2)
            elif op == op_gon:
                print("Es un empate, vuelvanlo a intentar")
            elif op not in [1, 2, 3]:
                print("No es una opcion")

    def level3(self):
        print(f"Felicitaciones {self.name}, haz logrado llegar a la tercera etapa del exámen de cazador. Un buen cazador debe tener buenos conocimientos de cultura general, en esta etapa evaluaremos tu nivel con 5 "
            f"preguntas, de las cuales solo es necesario dar 3 respuestas correctas para pasar a la siguiente etapa del examen")

        print("\n!!!!QUIZ!!!!")

        questions_list = ["Si 50 es el 100%, ¿cuánto es el 90%?",
                          "¿Cuál es el primero de la lista de los números primos?",
                          "¿Cuál es el río más largo del mundo?",
                          "¿Cuál es el océano más grande del mundo?",
                          "¿Cuál es el planeta más grande del Sistema Solar?"]

        answer_list = [{"a": "45", "b": "50", "c": "47.5"},
                       {"a": "1", "b": "2", "c": "3"},
                       {"a": "Amazonas", "b": "Nilo", "c": "Bravo"},
                       {"a": "Indico", "b": "Atlantico", "c": "Pacifico"},
                       {"a": "Mercurio", "b": "Jupiter", "c": "Neptuno"}]

        i = 0
        number_list = []
        rand = 0
        val = 0

        while i < 5:
            while rand in number_list:
                rand = random.randint(0, 4)

            print(str(i + 1) + ". " + questions_list[rand] + "\n")
            print("a) " + answer_list[rand]["a"] + "\tb) " + answer_list[rand]["b"] + "\tc) " + answer_list[rand]["c"] + "\n")
            res = input("Respuesta: ")

            if (rand == 0 and res == "a") or (rand == 1 and res == "b") or (rand == 2 and res == "a") or (rand == 3 and res == "c") or (rand == 4 and res == "b"):
                val += 1
                print(f"\nHaz respondido correctamente!!! :)\tPuntuacion: {val}\n")
            else:
                print(f"\nHaz respondido incorrectamente!!! :(\tPuntuacion: {val}\n")

            if val == 3:
                print("Enhorabuena, haz contestado 3 preguntas correctamente, puedes continuar a la 4ta etapa del examen de cazador")
                break

            number_list.append(rand)
            i += 1

        print("Que lastima, no lograste acertar ninguna pregunta, intentelo de nuevo")

    def level4(self):


    def level_completed(self, tag):
        print("\nDesea continuar a la siguiente etapa o volver al menu principal?")
        print("a) Continuar etapa\tb) Volver al menu")
        while True:
            res = input("-> ")
            if res == "a":
                if tag == 1:
                    self.level2()
                elif tag == 2:
                    self.level3()
            elif res == "b":
                print("Menu")
                break