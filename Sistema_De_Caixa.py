import datetime

agora = datetime.datetime.now()

hora = agora.strftime('%H:%M:%S')

print(hora)

total_ = 0
carrinho = []
total_venda = 0

catalogo = {
    101: ["Arroz 5kg", 25.00],
    102: ["Feijão 1kg", 9.50],
    103: ["Leite 1L", 5.19],
    104: ["Café 500g", 15.00]
}

