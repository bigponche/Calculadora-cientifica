import math
from requisitos import operadores, parentesis, factorial, OPERATOR_INFO, constantes

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
        if caracter == "-" and (tokens == [] or tokens[-1] in operadores or tokens[-1] in parentesis):
            valor , i = leer_numero(expresion,i+1)
            valor = "-"+ valor
        elif caracter.isdigit():
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


def es_mayor_o_igual_precedencia(pila_operadores, nuevo_operador):
    if pila_operadores == []:
        return False
    
    precedencia_arriba = OPERATOR_INFO[pila_operadores[-1]]['precedencia']
    precedencia_nuevo = OPERATOR_INFO[nuevo_operador]['precedencia']
    
    if precedencia_arriba > precedencia_nuevo:
        return True
    elif precedencia_arriba == precedencia_nuevo:
        if OPERATOR_INFO[nuevo_operador]['asociatividad'] == 'izquierda':
            return True
        else:
            return False
    else:
        return False
    
def procesar_cierre_parentesis(pila_operadores, salida):
    while pila_operadores[-1] != '(':
        operador_sacado = pila_operadores.pop()
        salida.append(operador_sacado)
    pila_operadores.pop()
    


def shunting_yard(tokens):
    pila_operadores = []
    salida = []
    
    for token in tokens:
        if token.replace('.', '', 1).replace('-','',1).isdigit() or token in constantes:
            salida.append(token)
        elif token == '(':
            pila_operadores.append(token)
        elif token == ')':
            procesar_cierre_parentesis(pila_operadores, salida)
        else:
            while pila_operadores != [] and pila_operadores[-1] != '(' and es_mayor_o_igual_precedencia(pila_operadores, token):
                operador_sacado = pila_operadores.pop()
                salida.append(operador_sacado)
            pila_operadores.append(token)
    while pila_operadores != []:
        agregado = pila_operadores.pop()
        salida.append(agregado)
    
    return salida


def evaluar_rpn(tokens_rpn):
    pila_numeros = []
    for token in tokens_rpn:
        if token.replace('.', '', 1).replace('-','',1).isdigit():
            numero = float(token)
            pila_numeros.append(numero)
        elif token.isalpha() and token in constantes:
            if token == "pi":
                pila_numeros.append(math.pi)
            elif token == 'e':
                pila_numeros.append(math.e)
            else:
                raise SyntaxError('No es un valor constante')
        elif token in ['sin', 'cos', 'tan', 'ln', 'log', 'sqrt']:
            
            operando = pila_numeros.pop()
            if token == 'sin':
                resultado = math.sin(operando)
            elif token == 'cos':
                resultado = math.cos(operando)
            elif token == 'tan':
                resultado = math.tan(operando)
            elif token == 'sqrt':
                if operando < 0:
                    raise ValueError('esto es un numero imaginario') # ← tu turno: validar que operando no sea negativo, y calcular la raíz
                else:
                    resultado = math.sqrt(operando)
            elif token == 'ln':
                if operando <= 0:
                    raise ValueError('logaritmo debe ser un numero > 0')
                else:
                    resultado = math.log(operando)
            elif token == 'log':
                if operando <= 0:
                    raise ValueError('logaritmo debe ser un numero > 0')
                else:
                    resultado = math.log10(operando)
            pila_numeros.append(resultado)
        elif token == '!':
            operando = pila_numeros.pop()   # el factorial solo saca UN número
            if operando != int(operando):
                raise ValueError("el factorial no puede ser un decimal")
            elif operando < 0:
                raise ValueError("el factorial no puede ser negativo")
            else:
                resultado=math.factorial(int(operando))
            # ← tu turno: calcular el factorial de "operando" y guardarlo en "resultado"
            pila_numeros.append(resultado)
        else:
            segundo_operando = pila_numeros.pop()
            primer_operando = pila_numeros.pop()
            if token == '+':
                resultado = primer_operando + segundo_operando
            elif token == '-':
                resultado = primer_operando - segundo_operando
            elif token == '*':
                resultado = primer_operando * segundo_operando
            elif token == '/':
                if segundo_operando == 0.0:
                    raise ZeroDivisionError('No puedes dividir entre cero')
                else:
                    resultado = primer_operando / segundo_operando
            elif token == '^':
                resultado = primer_operando ** segundo_operando
            elif token == '%':
                if segundo_operando == 0.0:
                    raise ZeroDivisionError('No puedes dividir entre cero')
                else:
                    resultado = primer_operando % segundo_operando
            pila_numeros.append(resultado)
    return pila_numeros.pop()