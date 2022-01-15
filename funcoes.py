def simplificado(fracoes):
    """
    Parâmetro: Uma lista contendo frações (em formato de string) 
    Return: Uma lista que pode conter números inteiros ou frações irredutíveis, ambos em formato de string.
    """
    simplificados = list()
    for fracao in fracoes:
        if 'sqrt' not in fracao and '/' in fracao:
            raiz = fracao.split('/')
            numerador = int(float(raiz[0]))
            denominador = int(float(raiz[1]))
            divisoesFeitas = 1
            while divisoesFeitas != 0:
                divisoesFeitas = 0
                for c in range(2, denominador + 1):
                    if denominador % c == 0 and numerador % c == 0:
                        numerador //= c
                        denominador //= c
                        divisoesFeitas += 1
            if denominador == 1:
                simplificados.append(str(numerador))
            elif denominador == -1:
                simplificados.append(str(-numerador))
            else:
                simplificados.append(f'{numerador}/{denominador}')
        else:
            simplificados.append(fracao)
    return simplificados


def bhaskara(expressao):
        """
        Parâmetro: Expressão contendo uma equação do segundo grau.
        Return: Uma tupla contendo duas raízes da equação.
        """
        from math import sqrt
        expressaoEmLista = list(expressao)
        coeficientes = list()
        for pos, char in enumerate(expressaoEmLista):
            if char == '(':
                novoCoficiente = ''
                posAtual = pos + 1
                while expressaoEmLista[posAtual] != ')':
                    novoCoficiente += expressaoEmLista[posAtual]
                    posAtual += 1 
                coeficientes.append(novoCoficiente)
        while 'x' in coeficientes:
            coeficientes.remove('x')
        a = float(coeficientes[0])
        b = float(coeficientes[1])
        c = float(coeficientes[2])
        delta = (b) ** 2 - 4 * a * c
        if delta >= 0 and int(sqrt(delta)) == sqrt(delta):
            x1 = f'{(-b + sqrt(delta))}/{2 * a}'
            x2 = f'{(-b - sqrt(delta))}/{2 * a}'
        else:
            x1 = f'(-{b} + sqrt({delta})) / {2 * a}'.replace('--', '+')
            x2 = f'(-{b} - sqrt({delta})) / {2 * a}'.replace('--', '+')
        return x1, x2


def briotRuffinne(coeficientes, raiz):
    """
    Parâmetro1: Uma lista com os coeficientes da equação.
    Parâmetro2: Uma raiz da equação.
    Return: Uma lista com os coeficientes da equação reduzida em um grau.
    """
    novosCoeficientes = list()
    for coeficiente in coeficientes:
        if len(novosCoeficientes) == 0:
            novosCoeficientes.append(coeficiente)
        else:
            novosCoeficientes.append(novosCoeficientes[-1] * eval(str(raiz)) + int(coeficiente))
    novosCoeficientes.pop()
    return novosCoeficientes
