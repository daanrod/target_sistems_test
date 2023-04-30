"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva 
um programa na linguagem que desejar onde, informado um número, ele calcule a sequência 
de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
previamente definido no código;
"""

if __name__ == "__main__":
    
    numero_procurado = 21

    fibo = [0,1]

    while fibo[-1] < numero_procurado:
        proximo_numero = fibo[-1] + fibo[-2]
        fibo.append(proximo_numero)

    if numero_procurado in fibo:
        (f"O numero {numero_procurado} pertence a sequencia de Fibonacci")
    else:
        (f"O numero {numero_procurado} não pertence a sequencia de Fibonacci")
