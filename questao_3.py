"""
3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""
from num2words import num2words


def format_list(list: list) -> str:
    return str(list).strip('[]')


if __name__ == "__main__":
    # Separador
    sep = ('- - - ' * 10)
    print(sep)

    # QUESTÃO 3.a
    # Logica: Os numeros estão sendo acrescidos pelo numero 2.

    # List comprehension com o laço "for"
    # -> iniciando em 1
    # -> indo até o range 10
    # -> pulando de 2 em 2 numeros
    sequencia_a = [n for n in range(1, 10, 2)]

    # Formatando a lista para string, para melhor leitura
    f_sequencia_a = format_list(sequencia_a)

    print(
        f"Resposta da questão 3.a:\n"
        f"  Logica: Os numeros estão sendo acrescidos pelo numero 2.\n"
        f"  A sequencia completa: a) {f_sequencia_a}\n"
        f"  Sendo o numero que completa a questão: {sequencia_a[-1]}"
    )

    print(sep)

    # QUESTÃO 3.b
    # Logica: O numero 2 esta sendo elevado ao numero de sequencia, partindo do numero 1.

    # List comprehension com o laço "for"
    # Com operação de exponenciação para cara item da lista
    sequencia_b = [2 ** n for n in range(1, 8)]

    # Formatando a lista para string, para melhor leitura
    f_sequencia_b = format_list(sequencia_b)

    print(
        f"Resposta da questão 3.b:\n"
        f"  Logica: O numero 2 esta sendo elevado ao numero de sequencia, partindo do numero 1.\n"
        f"  A sequencia completa: b) {f_sequencia_b}\n"
        f"  Sendo o numero que completa a questão: {sequencia_b[-1]}"
    )

    print(sep)

    # QUESTÃO 3.c
    # Logica: Cada numero da lista está sendo elevado ao numero 2.

    # List comprehension com o laço "for"
    # Com operação de exponenciação para cara item da lista
    sequencia_c = [n ** 2 for n in range(0, 8)]

    # Formatando a lista para string, para melhor leitura
    f_sequencia_c = format_list(sequencia_c)

    print(
        f"Resposta da questão 3.c:\n"
        f"  Logica: Cada numero da lista está sendo elevado ao numero 2.\n"
        f"  A sequencia completa: c) {f_sequencia_c}\n"
        f"  Sendo o numero que completa a questão: {sequencia_c[-1]}"
    )

    print(sep)

    # QUESTÃO 3.d
    # Logica: Somente numeros pares elevados ao quadrado.

    # List comprehension com o laço "for"
    # Com operação de exponenciação para cara item da lista
    sequencia_d = [n ** 2 for n in range(2, 12, 2)]

    # Formatando a lista para string, para melhor leitura
    f_sequencia_d = format_list(sequencia_d)

    print(
        f"Resposta da questão 3.d:\n"
        f"  Logica: cada numero da lista está sendo elevado ao numero 2.\n"
        f"  A sequencia completa: d) {f_sequencia_d}\n"
        f"  Sendo o numero que completa a questão: {sequencia_d[-1]}"
    )

    print(sep)

    # QUESTÃO 3.e
    # Logica: Sequencia de Fibonacci.

    sequencia_e = [1, 1]
    for i in range(2, 7):
        sequencia_e.append(sequencia_e[i-1] + sequencia_e[i-2])

    # Formatando a lista para string, para melhor leitura
    f_sequencia_e = format_list(sequencia_e)

    print(
        f"Resposta da questão 3.e:\n"
        f"  Logica: Sequencia de Fibonacci.\n"
        f"  A sequencia completa: e) {f_sequencia_e}\n"
        f"  Sendo o numero que completa a questão: {sequencia_e[-1]}"
    )

    print(sep)

    # QUESTÃO 3.f
    # Logica: Numeros começados com a letra D

    sequencia_f = []
    numero = 0

    while len(sequencia_f) < 8:
        numero += 1
        extenso = num2words(numero, lang='pt_BR')
        if extenso[0] == 'd':
            sequencia_f.append(numero)

    # Formatando a lista para string, para melhor leitura
    f_sequencia_f = format_list(sequencia_f)

    print(
        f"Resposta da questão 3.f:\n"
        f"  Logica: Numeros começados com a letra D.\n"
        f"  A sequencia completa: f) {f_sequencia_f}\n"
        f"  Sendo o numero que completa a questão: {sequencia_f[-1]}"
    )

    print(sep)
