from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizzaria', 'Gourmet')

bebida_suco = Bebida('Suco Laranja', 8.0, 'Grande')
prato_macarronada = Prato('Macarronada', 20.0, 'O melhor carbonara')
bebida_suco.aplicar_desconto()
prato_macarronada.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_macarronada)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()