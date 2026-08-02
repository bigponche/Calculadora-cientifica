from funciones import tokenizar, shunting_yard, evaluar_rpn

def calcular(expresion):
    
    tokens = tokenizar(expresion)
    rpn = shunting_yard(tokens)
    return evaluar_rpn(rpn)

if __name__ == "__main__":
    while True:
        entrada = input("Ingresá una expresión (o 'salir' para salir): ")
        if entrada == "salir":
            break
        try:
            resultado = calcular(entrada)
            print("Resultado:", resultado)
        except ValueError:
            print("Error: Dato incorrecto")  # ← tu turno: mensaje descriptivo
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0")
        except SyntaxError:
            print("Error: Sintaxis incorrecta")
