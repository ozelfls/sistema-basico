estoque = {}

def adicionarProduto(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f'{quantidade} unidades de {nome} adicionados ao estoque')


def atualizarProduto(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f'a quantidade de{nome} foi atualizada para {quantidade}')
    else:
        print(f'o produto {nome} não foi encontrado')


def exibirEstoque():
    print("\nEstoque Atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")


while True:
    print('\n1 - adicionar produto')
    print('2 - atualizar produto')
    print('3 - exibir estoque')
    print('4 - sair')
    escolha = input('escolha uma opção: ')
    
    if escolha == "1":
        nome = input('nome do produto: ')
        quantidade = int(input('quantidade: '))
        adicionarProduto(nome, quantidade)
    elif escolha == "2":
        nome = input('nome do produto: ')
        quantidade = int(input('nova quantidade: '))
        atualizarProduto(nome, quantidade)
    elif escolha == "3":
        exibirEstoque()
    elif escolha == "4":
        print('encerrando sistema...')
        break
    else:
        print('opção invalida, tente novamente mais tarde: ')
