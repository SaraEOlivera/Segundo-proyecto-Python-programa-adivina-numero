import random

def subrayar_titulo(titulo, caracter = "="):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))


def programa_adivinador_de_numero(x):


    print(f"Pensá un número entre 1 y {x} y el programa intentará adivinarlo.")

    valor_minimo = 1
    valor_maximo = x
    mi_respuesta = ""
    while mi_respuesta != "c":
        #generar intento:
        if valor_minimo != valor_maximo:
            intento_computadora = random.randint(valor_minimo, valor_maximo)
        else: 
            intento_computadora = valor_maximo

        #responder si adivinó
        print()
        mi_respuesta = input(f"El número que pensaste es {intento_computadora}. Si mi predicción es mayor a tu numero, ingresá (A). Si es muy menor, ingresá (B) y si adiviné ingresá (C): ").lower()

        if mi_respuesta == "a":
            valor_maximo = intento_computadora - 1
        elif mi_respuesta == "b":
            valor_minimo = intento_computadora + 1

    print(f"¡¡Adiviné!! El numero que estabas pensando era {intento_computadora}")

subrayar_titulo("¡¡Bienvenido al juego!!")
programa_adivinador_de_numero(15)


