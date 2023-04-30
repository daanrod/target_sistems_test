"""
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de 
Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na 
rodovia, qual estará mais próximo a cidade de Ribeirão Preto?


IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.
"""

if __name__ == "__main__":
    # Distancia entre as cidades em km
    distancia_cidades = 100

    # Velocidade do carro em km/h
    velocidade_carro = 110

    # Velocidade do caminhao em km/h
    velocidade_caminhao = 80

    # Tempo em horas para o caminhao chegar ao ponto de encontro
    tempo_caminhao = distancia_cidades / \
        (velocidade_carro + velocidade_caminhao)

    # Tempo em horas para o carro chegar ao ponto de encontro
    tempo_carro = distancia_cidades / velocidade_carro

    # Distancia percorrida pelo caminhao ate o ponto de encontro
    distancia_caminhao = velocidade_caminhao * tempo_caminhao

    # Distancia percorrida pelo carro ate o ponto de encontro
    distancia_carro = velocidade_carro * tempo_carro

    # Distancia da cidade de Ribeirao Preto ate o ponto de encontro
    distancia_rp = distancia_cidades - distancia_carro

    # Distancia da cidade de Franca ate o ponto de encontro
    distancia_franca = distancia_cidades - distancia_caminhao

    # verifica qual veículo está mais próximo de Ribeirao Preto
    if distancia_rp < distancia_franca:
        print("O carro está mais próximo de Ribeirao Preto.")
    else:
        print("O caminhao está mais próximo de Ribeirao Preto.")

    print('Cheguei ao resultado utilizando a formula "distancia = velocidade x tempo"')
