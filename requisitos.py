operadores = ['+','-','*','/','^','%']
parentesis = ['(',')']
funciones = ['sin','cos','tan','ln','log','sqrt']
constantes = ['pi','e']
factorial = ['!']

OPERATOR_INFO = {
    '+': {'precedencia': 1 ,'asociatividad' : 'izquierda'},
    '-': {'precedencia': 1,'asociatividad' : 'izquierda'},
    '*': {'precedencia': 2,'asociatividad' : 'izquierda'},
    '/': {'precedencia': 2,'asociatividad' : 'izquierda'},
    '%': {'precedencia': 2,'asociatividad' : 'izquierda'},
    '^': {'precedencia': 3,'asociatividad' : 'derecha'},
    '!': {'precedencia': 4,'asociatividad' : 'no aplica'},
    'sin': {'precedencia': 5,'asociatividad' : 'no aplica'},
    'cos': {'precedencia': 5,'asociatividad' : 'no aplica'},
    'tan': {'precedencia': 5,'asociatividad' : 'no aplica'},
    'ln': {'precedencia': 5,'asociatividad' : 'no aplica'},
    'log': {'precedencia': 5,'asociatividad' : 'no aplica'},
    'sqrt': {'precedencia': 5,'asociatividad' : 'no aplica'},
    
}

ERRORES_INFO = ['1/0 = division entre 0','(2+3 = error de sintaxis','10^10000=numeros muy grandes', 
                '@= simbolo no encontrado', 'sqrt -9=raiz de numero negativo', '-5! = factorial negativo',
                '3.5! = factorial numero decimal', 'log(-20) = logaritmo numero negativo']