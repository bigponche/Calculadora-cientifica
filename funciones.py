
def leer_numero(expresion,inicio):
    i=inicio
    resultado=""
    contador= 0
    while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
        if expresion[i] == "." and contador <2:
            contador +=1
            if contador >= 2:
                raise SyntaxError('estas usando mas de 2 simbolos .')
        resultado += expresion[i]
        i += 1
    return resultado, i

print(leer_numero("23+4",0))
print(leer_numero("3.5*2",0))
print(leer_numero("sin(90",4))

def leer_palabra(expresion,inicio):
    i= inicio
    resultado = ""
    while i < len(expresion) and expresion[i].isalpha():
        resultado +=expresion[i]
        i +=1
    return resultado, i

leer_palabra("sin(90)", 0)
leer_palabra("pi+5", 0)
leer_palabra("cos(0)+sin(0)", 7)