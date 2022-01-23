from funcoes import *
class Equacao(object):
    """
    Classe que armazena uma equação polinomial de qualquer grau.
    """
    def __init__(self, coeficientes):
        """
        Recebe os coeficientes da equação (em ordem crescente).
        """
        self.coeficientes = coeficientes

    
    def __repr__(self) -> str:
        """
        Retorna uma representação da equação. 
        """
        expressao = ''

        for pos, coeficiente in enumerate(self.coeficientes):
            e = len(self.coeficientes) - pos - 1
            expressao += f'({coeficiente}) * (x)**{e} + '
        expressao  = expressao.replace(' * (x)**0 + ', ' = 0')

        return expressao

    def e_raiz(self, raiz):
        """
        Calcula se um valor pode ser raiz da equação.
        """
        return eval(self.__repr__().replace(' = 0', ' == 0').replace('x', str(raiz)))


    def possiveisRaizesReais(self):
        """
        Retorna uma lista com os valores reais candidatos a serem uma raiz da equação.
        """
        termoMaiorGrau = int(self.coeficientes[0])
        termoIndependente = int(self.coeficientes[-1])
        divisoresTermoIndependente = list()
        divisoresTermoMaiorGrau = list()
        for c in range(1, abs(termoIndependente) + 1):
            if termoIndependente % c == 0:
                divisoresTermoIndependente.append(c)
                divisoresTermoIndependente.append(-c)
        for c in range(1, abs(termoMaiorGrau) + 1):
            if termoIndependente % c == 0:
                divisoresTermoMaiorGrau.append(c)
                divisoresTermoMaiorGrau.append(-c)

        possiveisRaizes = list()
        for numerador in divisoresTermoIndependente:
            for denominador in divisoresTermoMaiorGrau:
                possiveisRaizes.append(f'{numerador}/{denominador}')
        possiveisRaizes.append('0')

        return possiveisRaizes

    
    def raizes(self):
        """
        Calcula as raízes da equação e as retorna em uma lista.
        """
        testes = self.possiveisRaizesReais()
        expressao = self
        coeficientes = self.coeficientes
        raizes = list()
        while len(coeficientes) > 3:
            for teste in testes:
                if self.e_raiz(teste):
                    raizes.append(teste)
                    novosCoeficientes = briotRuffinne(coeficientes, teste)
                    expressao = Equacao(novosCoeficientes)
                    coeficientes = expressao.coeficientes
                    if teste == '0':
                        testes = expressao.possiveisRaizesReais()
                    break
            else:
                break

        if len(coeficientes) == 3:
            raizesRestantes = bhaskara(expressao.__repr__().replace(' = 0', ''))
            raizes.append(raizesRestantes[0])
            raizes.append(raizesRestantes[1])
        elif len(coeficientes) == 2:
            raizes.append(f'{-coeficientes[1]}/{coeficientes[0]}')

        return simplificado(raizes)

if __name__ == '__main__':
    while True:
        try:
            coeficientes = list()
            grauDaEquacao = int(input('Qual o grau da equação? '))
            for c in range(grauDaEquacao):
                e = grauDaEquacao - c
                coeficiente = float(input(f'Digite o coeficiente do x**{e}: '))
                coeficientes.append(coeficiente)
            termoIndependente = float(input('Digite o termo independente: '))
            coeficientes.append(termoIndependente)

            equacao = Equacao(coeficientes)
            raizes = equacao.raizes()
            
            print('S = {', end='')
            for pos, raiz in enumerate(raizes):
                if pos == len(raizes) - 1:
                    print(raiz, end='}\n')
                else:
                    print(raiz, end=', ')
            if len(raizes) == 0:
                print('}')

        except KeyboardInterrupt:
            print('\nPrograma finalizado!')
            break
