import os
import cowsay
from asciimatics.effects import Print, Scroll
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from pydub import AudioSegment
from pydub.playback import play

# Diccionari inicial buit
diccionari = {}



# Funció per afegir una paraula i les seves accepcions al diccionari
def afegir_paraula(paraula, accepcions):
    diccionari[paraula] = accepcions

# Funció per afegir una accepció a una paraula existent
def afegir_accepcio(paraula, accepcio, definicio):
    if paraula in diccionari:
        diccionari[paraula][accepcio] = definicio
    else:
        print("La paraula no existeix al diccionari.")

# Funció per mostrar totes les paraules i les seves accepcions
def mostrar_diccionari():
    for paraula, accepcions in diccionari.items():
        print(f"{paraula}:")
        for accepcio, definicio in accepcions.items():
            print(f" - {accepcio}: {definicio}")

# Funció per mostrar la portada animada
def mostrar_portada():
    title = """
  ____  _      _        _                        _              
|  _ \(_) ___| | _____(_) ___  _ __   __ _ _ __(_)     ___   __
| | | | |/ __| |/ / __| |/ _ \| '_ \ / _` | '__| |    (_) \ / /
| |_| | | (__|   < (__| | (_) | | | | (_| | |  | |     _ \ V / 
|____/|_|\___|_|\_\___|_|\___/|_| |_|\__,_|_|  |_|    (_) \_/  
 """
    scenes = []
    effects = [
        Print(
            Screen().printer,
            Scroll(title, speed=1),
            x=Screen().width // 2 - 40,
            y=Screen().height // 2 - 5,
            transparent=False
        )
    ]
    scenes.append(Scene(effects, -1))
    screen = Screen.open()
    screen.play(scenes, stop_on_resize=True)

# Funció principal de l'aplicació
def main():
    # Mostrem la portada
    mostrar_portada()

    # Introduir la paraula "xarxa" amb les dues entrades
    paraula = "xarxa"
    entrada1 = {"PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}
    entrada2 = {"TÈXTIL": "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà."}

    afegir_paraula(paraula, entrada1)
    afegir_accepcio(paraula, "TÈXTIL", "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà.")

    while True:
        print("\n********** Menú **********")
        print("1. Afegir paraula")
        print("2. Afegir accepcio")
        print("3. Mostrar diccionari")
        print("4. Sortir")

        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            paraula = input("Introdueix la paraula: ")
            accepcio = input("Introdueix l'accepcio: ")
            definicio = input("Introdueix la definicio: ")
            if paraula not in diccionari:
                diccionari[paraula] = {accepcio: definicio}
            else:
                diccionari[paraula][accepcio] = definicio
            print("Paraula i accepcio afegides correctament.")
        elif opcio == "2":
            paraula = input("Introdueix la paraula a la qual vols afegir l'accepcio: ")
            if paraula in diccionari:
                accepcio = input("Introdueix l'accepcio: ")
                definicio = input("Introdueix la definicio: ")
                diccionari[paraula][accepcio] = definicio
                print("Accepcio afegida correctament.")
            else:
                print("La paraula no existeix al diccionari.")
        elif opcio == "3":
            print("\n********** Diccionari **********")
            mostrar_diccionari()
        elif opcio == "4":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

if __name__ == "__main__":
    main()