from requisitos import operadores, parentesis, factorial

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

def leer_simbolo(expresion,inicio):
    i=inicio
    if expresion[i] in operadores or expresion[i] in parentesis or expresion[i] in factorial:
        resultado=expresion[i]
        i += 1
    else:
        raise SyntaxError('el operador no es valido')
    return resultado,i

def tokenizar(expresion):
    i = 0
    tokens = []
    while i < len(expresion):
        caracter = expresion[i]
        if caracter.isdigit():
            valor, i = leer_numero(expresion, i)
        elif caracter.isalpha():
            valor, i = leer_palabra(expresion, i)
        elif caracter in operadores or caracter in parentesis or caracter in factorial:
            valor, i = leer_simbolo(expresion, i)
        elif caracter==" ":
            i += 1
            continue
        else:
            raise SyntaxError('introduciste un valor invalido')
        tokens.append(valor)
    return tokens