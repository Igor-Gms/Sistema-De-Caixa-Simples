import datetime

agora = datetime.datetime.now()

hora = agora.strftime('%H:%M:%S')

carrinho = []
total_venda = 0

catalogo = {
    101: ["Arroz 5kg", 25.00],
    102: ["Feijão 1kg", 9.50],
    103: ["Leite 1L", 3.79],
    104: ["Café 500g", 26.98],
    105: ["Açucar 5kg", 16.90],
    106: ["Óleo de Soja 900ml", 6.79],
    107: ["Pão De Forma 400g", 5.69],
    108: ["Manteiga 200g",10.20],
    109: ["Cartela De Ovos 20un", 17.90],
    110: ["Sal Refinado 1kg", 3.79],
    111: ["Refrigerante Guaraná 2L", 8.79]

}
def mostrar_catalogo():
    print("===== Catálogo De Produtos =====")

    for codigo,(nome, preco) in catalogo.items(): # mostras os produtos de forma mais facil de entender

        print(f"Codigo: {codigo} | Produto: {nome} | Preço:R$ {preco:.2f}")
print()

mostrar_catalogo()

while True:
 carrinho1 = int(input("\nEscolha Os Produtos De Acordo Com Os Códigos(Digite 0 Para Finalizar a Compra):"))
 if carrinho1 == 0:
  print("Compra Finalizada.")
  break
 
 #Remover 1 Unidade Do Item Correspondente Do Carrinho
 elif carrinho1 < 0:
   codigo_para_remover = abs(carrinho1) #abs transforma o codigo em negativo(101 para -101)
   
   if codigo_para_remover in carrinho:
     carrinho.remove(codigo_para_remover)
     print(f"REMOVIDO: {catalogo[codigo_para_remover][0]} Saiu Do Carrinho.")

   else:
     print("Este Produto Não Está No Seu Carrinho")

 elif 101 <= carrinho1 <= 111 :
  carrinho.append(carrinho1) #colocar no carrinho os codigo que a pessoa 
  print(f"Você Adicionou -- {catalogo[carrinho1][0]} no carrinho")
 else:
   print("Código Inválido")

for codigo in carrinho: # fazer a soma dos prodotos
 total_venda += catalogo [codigo][1]

if total_venda == 0:# saber se a pessoa escolheu algum produto
 print("você não escolheu nenhum produto.")
else:
 print(f"Total da compra:{total_venda}")
        
