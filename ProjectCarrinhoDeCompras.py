cart = []

# cria uma lista vazia chamada 'cart'

catalog = [
    {"id": 55, "nome": "Airpod", "preco": 50.0, "quantidade": 1},
    {"id": 1243, "nome": "PC Gamer", "preco": 5000.0, "quantidade": 1},
    {"id": 256, "nome": "Fone sem fio", "preco": 150.0, "quantidade": 1},
    {"id": 541, "nome": "Iphone 16", "preco": 20000.0, "quantidade": 1},
    {"id": 13, "nome": "Nokia", "preco": 135.50, "quantidade": 1},
    {"id": 45, "nome": "Monitor 19", "preco": 700.0, "quantidade": 1},
    {"id": 698, "nome": "TV Samsung 4k 75", "preco": 5700.0, "quantidade": 1},
    {"id": 908, "nome": "Mouse Razzer", "preco": 99.99, "quantidade": 1},
    {"id": 258, "nome": "Tablet CCE", "preco": 450.0, "quantidade": 1},
    {"id": 157, "nome": "Copo stanley", "preco": 300.0, "quantidade": 1},
]


# cria uma lista chamada 'catalog' cuja cada posição(index) é prenchida por um dicionário
# cada dicionário é um produto com chaves 'id', 'nome', 'preco' e 'quantidade'

def get_product(id_select):
    for product in catalog:
        if id_select == product["id"]:
            return product


# cria função para obter o produto selecionado
# vasculha a lista 'catalog' e armazena na variável 'product' um dicionario da lista por iteração
# verifica se o parametro passado corresponde a chave 'id' do dicionario atual
# true: retorna para essa função o dicionário correspondente ao parametro
''''Para cada index de catalogo a variável produto recebe o valor presente nesse index
e então verifica se esse é igual ao valor passado pelo parametro da função'''


def add_product(id_select):
    product = get_product(id_select)
    cart.append(product)


# cria função para adicionar o produto selecionado ao carrinho de compras
# cria a variável 'product' para chamar a função 'get_product' e receber o produto selecionado
# usa uma função de lista para adicionar o valor de retorno da função 'get_product' a lista 'cart'

def remove_product(id_select):
    product = get_product(id_select)
    cart.remove(product)


# cria função para remover o produto selecionado do carrinho de compras
# cria a variável 'product' para chamar a função 'get_product' e receber o produto selecionado
# usa uma função de lista para remover o valor de retorno da função 'get_product' da lista 'cart'

def payment_conditions(purchase_abroad, installment_purchase, number_of_installments):
    total = calculate_total()
    if purchase_abroad and total > 200.00:
        total += (total * 0.05)
    if number_of_installments > 12 or number_of_installments == 1:
        return total
    if installment_purchase:
        installments = total / number_of_installments
        print(f'Parcelado em {number_of_installments} vezes: Valor parcela = R${installments:.2f}')
    return total


# cria função para determinar condições do pagamento na finalização da compra
# cria variável 'total' para receber o chamado da função 'calculate_total' e receber a soma total do carrinho
# verifica se a condição 'purchase_abroad' e 'total>200' é verdadeira
# true: a variável total é aumentada com uma taxa de 5%
# verifica se a condição 'installment_purchase' é verdadeira
# true: cria variável 'installments' que recebe o 'total' divido pelo 'number_of_installments'
# imprime na tela a mensagem extra
# função retorna o total


def calculate_total():
    total = 0.0
    for product in cart:
        product_price = product["preco"]
        total += product_price
    return total


# cria função para calcular a soma total dos itens do carrinho de compras
# cria a variável 'total' e determina seu valor inicial como zero
# vasculha a lista 'cart' e armazena na variável 'product' um dicionario da lista por iteração
# cria a variável 'product_price' e armazena nela a o valor da chave 'preco' do dicionário atual
# acumula na variável 'total' os valores correspondetes a chave de 'preco' de cada dicionario presente em 'cart'
# retorna o valor acumulado 'total'
'''Para cada index da lista carrinho ele adiciona numa variavel de controle o total dos valores referentes as chaves
de preço dos produtos'''


def calculate_amount(id_select):
    amount = 0
    for product in cart:
        if id_select == product["id"] and cart.count(product) >= 1:
            product_amount = product["quantidade"]
            amount += product_amount
    return amount


# cria função para calcular a quantidade de um dado produto dentro do carrinho de compras
# cria a variável 'amount' e determina seu valor inicial como zero
# vasculha a lista 'cart' e armazena na variável 'product' um dicionario da lista por iteração
# verifica se o parametro 'id_select' é igual a chave 'id' do produto atual
# true: verifica através da função 'count' se a quantidade de produtos iguais ao atual dentro de 'cart' é maior ou
# igual a 1
# true: cria a variável 'product_amount' e armazena nela o valor da chave 'quantidade' do dicionario atual
# acumula na variável 'amount' os valores correspondetes a chave 'quantidade' de cada dicionário atual
# retorna o valor acumulado 'amount'
'''No primeiro loop do for ele faz product receber o dicionario na primeira posição do cart, após isso ele verifica
se a chave id desse dicionario é correspondente ao parametro id_select, se for ele verifica se a quantidade de 
dicionarios iguais este que existem em cart é maior ou igual a 1, se for ele armazena na variável product_amount o 
valor da chave quantidade do dicionario, somando esse valor na variável amount que é então incrementada a cada 
iteração em que essas condições permanecem verdadeiras'''

# simulação front-end
add_product(55)
add_product(1243)

# mostra valores e condições de compra
print(f'O total da sua compra foi de R${payment_conditions(False, True, 2):.2f}')
# index 0: se ele é de fora do brasil ou não
# index 1: se ele quer parcelar ou não
# index 2: em quantas parcelas ele vai fazer
