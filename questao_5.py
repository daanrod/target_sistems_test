"""
5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

if __name__ == "__main__":
    
    string_original = "Target Sistems"

    string_invertida = ""

    # Percorrendo a string de tras para frente e concatenando cada caractere na nova string
    for i in range(len(string_original)-1, -1, -1):
        string_invertida += string_original[i]

    print(string_invertida)
