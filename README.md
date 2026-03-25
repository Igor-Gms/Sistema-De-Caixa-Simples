# 🛒 Sistema de Carrinho de Compras (CLI em Python)


\

Um sistema simples de carrinho de compras via terminal, desenvolvido em Python. Ideal para treinar lógica de programação, estruturas de dados e interação com o usuário.

---

## 📸 Demonstração

```bash
===== Catálogo De Produtos =====
Codigo: 101 | Produto: Arroz 5kg | Preço: R$ 25.00
Codigo: 102 | Produto: Feijão 1kg | Preço: R$ 9.50
...

Escolha Os Produtos De Acordo Com Os Códigos:
```

---

## 🚀 Funcionalidades

✅ Exibição de catálogo de produtos
✅ Adição e remoção de itens do carrinho
✅ Cálculo automático do total
✅ Desconto de **10% (Dinheiro e PIX)**
✅ Cálculo de média dos produtos
✅ Registro de horário da compra
✅ Cálculo de troco
✅ Tratamento de erros de entrada

---

## 🧾 Como funciona

* Digite o **código do produto** para adicionar ao carrinho
* Digite um código **negativo** para remover (`-101`)
* Digite `0` para finalizar a compra
* Escolha a forma de pagamento:

  * `1` → Dinheiro 💵 *(10% de desconto)*
  * `2` → Cartão 💳
  * `3` → PIX ⚡ *(10% de desconto)*

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta

```bash
cd seu-repositorio
```

### 3. Execute o projeto

```bash
python main.py
```

---

## 🛠️ Tecnologias

* Python 3
* Bibliotecas padrão:

  * `statistics`
  * `os`
  * `datetime`

---

## 🧠 Estrutura do código

* `catalogo` → dicionário com produtos e preços
* `carrinho` → lista com itens selecionados
* `total_venda` → soma total dos produtos
* `lista_precos` → usada para cálculo da média

---

## ⚠️ Tratamento de erros

O sistema evita falhas comuns como:

* Entrada de letras no lugar de números
* Códigos inválidos
* Remoção de itens inexistentes
* Pagamento insuficiente

---

## 📊 Exemplo de saída final

```bash
Inicio: 24/03/2026 14:00:00
Fim:    24/03/2026 14:05:00
========================================
Subtotal: R$ 50.00
----------------------------------------
Média Dos Preços Por Produto: R$ 10.00
----------------------------------------
Desconto (10%): - R$ 5.00
----------------------------------------
Total da compra: R$ 45.00
----------------------------------------
Forma de Pagamento: PIX
```

---

## 🚀 Melhorias futuras

* [ ] Interface gráfica (Tkinter ou Web)
* [ ] Banco de dados
* [ ] Cadastro de produtos dinâmico
* [ ] Controle de estoque
* [ ] Relatórios de vendas

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

---

## 👨‍💻 Autor

Desenvolvido por **Seu Nome Aqui**

💡 Projeto focado em aprendizado de Python e lógica de programação.

---

## ⭐ Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests!

Se esse projeto te ajudou, deixe uma ⭐ no repositório!
