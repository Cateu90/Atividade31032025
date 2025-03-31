from pydantic import ValidationError
from tabulate import tabulate
from produtos.produto_repo import ProdutoRepo
from produtos.produto import Produto
from comandas.comanda_repo import ComandaRepo
from comandas.comanda import Comanda
from caixas.caixa_repo import CaixaRepo
from caixas.caixa import Caixa
from datetime import datetime

def exibir_menu():
    """Exibe o menu principal de opções no console."""
    print("\n--- Menu de Gerenciamento do Restaurante ---")
    print("a) Cadastrar Produto")
    print("b) Listar Produtos")
    print("c) Alterar Produto")
    print("d) Excluir Produto")
    print("e) Cadastrar Comanda")
    print("f) Listar Comandas")
    print("g) Alterar Comanda")
    print("h) Excluir Comanda")
    print("i) Abrir Caixa")
    print("j) Listar Caixas")
    print("k) Fechar Caixa")
    print("l) Excluir Caixa")
    print("m) Sair")
    print("-----------------------------------------")

def obter_entrada_usuario(mensagem, tipo=str):
    """
    Solicita uma entrada do usuário, com validação de tipo.
    Repete a solicitação até que uma entrada válida seja fornecida.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.
        tipo (type): O tipo de dado esperado (str, float, int).

    Returns:
        O valor convertido para o tipo especificado.
    """
    while True:
        entrada = input(mensagem)
        try:
            if tipo == float:
                return float(entrada)
            elif tipo == int:
                return int(entrada)
            elif tipo == datetime:
                return datetime.fromisoformat(entrada)
            else:
                return entrada.strip()
        except ValueError:
            print(f"Entrada inválida. Por favor, insira um valor do tipo '{tipo.__name__}'.")

def cadastrar_produto(repo: ProdutoRepo):
    """Função para lidar com a opção de cadastrar um novo produto."""
    print("\n--- Cadastro de Novo Produto ---")
    try:
        nome = obter_entrada_usuario("Nome: ")
        preco = obter_entrada_usuario("Preço: ", float)
        estoque = obter_entrada_usuario("Estoque: ", int)

        novo_produto = Produto(nome=nome, preco=preco, estoque=estoque)

        produto_id = repo.adicionar(novo_produto)

        if produto_id:
            print(f"Produto '{novo_produto.nome}' cadastrado com sucesso! ID: {produto_id}")
        else:
            print("Falha ao cadastrar o produto.")

    except ValidationError as e:
        print("\nErro de validação ao cadastrar produto:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao cadastrar: {e}")

def listar_produtos(repo: ProdutoRepo):
    """Função para lidar com a opção de listar todos os produtos."""
    print("\n--- Lista de Produtos Cadastrados ---")
    produtos = repo.obter_todos()

    if produtos:
        tabela = [[p.id, p.nome, f"R$ {p.preco:.2f}", p.estoque] for p in produtos]
        cabecalhos = ["ID", "Nome", "Preço", "Estoque"]
        print(tabulate(tabela, headers=cabecalhos, tablefmt="grid", numalign="right", stralign="left"))
    else:
        print("Nenhum produto cadastrado.")

def alterar_produto(repo: ProdutoRepo):
    """Função para lidar com a opção de alterar um produto existente."""
    print("\n--- Alteração de Produto ---")
    try:
        produto_id = obter_entrada_usuario("ID do produto a ser alterado: ", int)
        produto_existente = repo.obter(produto_id)

        if produto_existente:
            print("\nDados atuais do produto:")
            print(f"  Nome: {produto_existente.nome}")
            print(f"  Preço: R$ {produto_existente.preco:.2f}")
            print(f"  Estoque: {produto_existente.estoque}")
            print("\nDigite os novos dados (deixe em branco para manter o valor atual):")

            nome = obter_entrada_usuario(f"Novo Nome ({produto_existente.nome}): ") or produto_existente.nome
            preco_str = obter_entrada_usuario(f"Novo Preço ({produto_existente.preco:.2f}): ")
            preco = float(preco_str) if preco_str else produto_existente.preco

            estoque_str = obter_entrada_usuario(f"Novo Estoque ({produto_existente.estoque}): ")
            estoque = int(estoque_str) if estoque_str else produto_existente.estoque

            produto_atualizado = Produto(id=produto_existente.id, nome=nome, preco=preco, estoque=estoque)

            if repo.atualizar(produto_atualizado):
                print(f"Produto ID {produto_id} atualizado com sucesso!")
            else:
                print(f"Falha ao atualizar o produto ID {produto_id}.")

        else:
            print(f"Produto com ID {produto_id} não encontrado.")

    except ValidationError as e:
        print("\nErro de validação ao alterar produto:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except ValueError:
         print("Entrada inválida para ID, preço ou estoque. A alteração foi cancelada.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao alterar: {e}")

def excluir_produto(repo: ProdutoRepo):
    """Função para lidar com a opção de excluir um produto."""
    print("\n--- Exclusão de Produto ---")
    try:
        produto_id = obter_entrada_usuario("ID do produto a ser excluído: ", int)

        produto = repo.obter(produto_id)
        if not produto:
             print(f"Produto com ID {produto_id} não encontrado.")
             return

        confirmacao = input(f"Tem certeza que deseja excluir o produto '{produto.nome}' (ID: {produto_id})? (s/N): ").lower()

        if confirmacao == 's':
            if repo.excluir(produto_id):
                print(f"Produto ID {produto_id} excluído com sucesso.")
            else:
                print(f"Falha ao excluir o produto ID {produto_id}. Pode já ter sido removido.")
        else:
            print("Exclusão cancelada.")

    except ValueError:
         print("ID inválido. A exclusão foi cancelada.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao excluir: {e}")

def cadastrar_comanda(repo: ComandaRepo):
    """Função para lidar com a opção de cadastrar uma nova comanda."""
    print("\n--- Cadastro de Nova Comanda ---")
    try:
        numero = obter_entrada_usuario("Número da comanda: ", int)
        data_abertura = obter_entrada_usuario("Data e hora de abertura (AAAA-MM-DD HH:MM:SS): ", datetime)

        nova_comanda = Comanda(numero=numero, data_abertura=data_abertura)

        comanda_id = repo.adicionar(nova_comanda)

        if comanda_id:
            print(f"Comanda número '{nova_comanda.numero}' cadastrada com sucesso! ID: {comanda_id}")
        else:
            print("Falha ao cadastrar a comanda.")

    except ValidationError as e:
        print("\nErro de validação ao cadastrar comanda:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao cadastrar: {e}")

def listar_comandas(repo: ComandaRepo):
    """Função para lidar com a opção de listar todas as comandas."""
    print("\n--- Lista de Comandas Cadastradas ---")
    comandas = repo.obter_todos()

    if comandas:
        tabela = [[c.id, c.numero, c.data_abertura, c.data_fechamento, f"R$ {c.valor_total:.2f}"] for c in comandas]
        cabecalhos = ["ID", "Número", "Data Abertura", "Data Fechamento", "Valor Total"]
        print(tabulate(tabela, headers=cabecalhos, tablefmt="grid", numalign="right", stralign="left"))
    else:
        print("Nenhuma comanda cadastrada.")

def alterar_comanda(repo: ComandaRepo):
    """Função para lidar com a opção de alterar uma comanda existente."""
    print("\n--- Alteração de Comanda ---")
    try:
        comanda_id = obter_entrada_usuario("ID da comanda a ser alterada: ", int)
        comanda_existente = repo.obter(comanda_id)

        if comanda_existente:
            print("\nDados atuais da comanda:")
            print(f"  Número: {comanda_existente.numero}")
            print(f"  Data Abertura: {comanda_existente.data_abertura}")
            print(f"  Data Fechamento: {comanda_existente.data_fechamento}")
            print(f"  Valor Total: R$ {comanda_existente.valor_total:.2f}")
            print("\nDigite os novos dados (deixe em branco para manter o valor atual):")

            numero_str = obter_entrada_usuario(f"Novo Número ({comanda_existente.numero}): ")
            numero = int(numero_str) if numero_str else comanda_existente.numero

            data_abertura_str = obter_entrada_usuario(f"Nova Data Abertura ({comanda_existente.data_abertura}): ")
            data_abertura = datetime.fromisoformat(data_abertura_str) if data_abertura_str else comanda_existente.data_abertura

            data_fechamento_str = obter_entrada_usuario(f"Nova Data Fechamento ({comanda_existente.data_fechamento}): ")
            data_fechamento = datetime.fromisoformat(data_fechamento_str) if data_fechamento_str else comanda_existente.data_fechamento

            valor_total_str = obter_entrada_usuario(f"Novo Valor Total ({comanda_existente.valor_total:.2f}): ")
            valor_total = float(valor_total_str) if valor_total_str else comanda_existente.valor_total

            comanda_atualizada = Comanda(id=comanda_existente.id, numero=numero, data_abertura=data_abertura, data_fechamento=data_fechamento, valor_total=valor_total)

            if repo.atualizar(comanda_atualizada):
                print(f"Comanda ID {comanda_id} atualizada com sucesso!")
            else:
                print(f"Falha ao atualizar a comanda ID {comanda_id}.")

        else:
            print(f"Comanda com ID {comanda_id} não encontrada.")

    except ValidationError as e:
        print("\nErro de validação ao alterar comanda:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except ValueError:
         print("Entrada inválida para ID, número, data ou valor. A alteração foi cancelada.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao alterar: {e}")

def excluir_comanda(repo: ComandaRepo):
    """Função para lidar com a opção de excluir uma comanda."""
    print("\n--- Exclusão de Comanda ---")
    try:
        comanda_id = obter_entrada_usuario("ID da comanda a ser excluída: ", int)

        comanda = repo.obter(comanda_id)
        if not comanda:
             print(f"Comanda com ID {comanda_id} não encontrada.")
             return

        confirmacao = input(f"Tem certeza que deseja excluir a comanda '{comanda.numero}' (ID: {comanda_id})? (s/N): ").lower()

        if confirmacao == 's':
            if repo.excluir(comanda_id):
                print(f"Comanda ID {comanda_id} excluída com sucesso.")
            else:
                print(f"Falha ao excluir a comanda ID {comanda_id}. Pode já ter sido removida.")
        else:
            print("Exclusão cancelada.")

    except ValueError:
         print("ID inválido. A exclusão foi cancelada.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao excluir: {e}")

def abrir_caixa(repo: CaixaRepo):
    """Função para lidar com a opção de abrir um novo caixa."""
    print("\n--- Abertura de Caixa ---")
    try:
        data_abertura = obter_entrada_usuario("Data e hora de abertura (AAAA-MM-DD HH:MM:SS): ", datetime)
        valor_inicial = obter_entrada_usuario("Valor inicial do caixa: ", float)

        novo_caixa = Caixa(data_abertura=data_abertura, valor_inicial=valor_inicial)

        caixa_id = repo.adicionar(novo_caixa)

        if caixa_id:
            print(f"Caixa aberto com sucesso! ID: {caixa_id}")
        else:
            print("Falha ao abrir o caixa.")

    except ValidationError as e:
        print("\nErro de validação ao abrir caixa:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao abrir o caixa: {e}")

def listar_caixas(repo: CaixaRepo):
    """Função para lidar com a opção de listar todos os caixas."""
    print("\n--- Lista de Caixas ---")
    caixas = repo.obter_todos()

    if caixas:
        tabela = [[cx.id, cx.data_abertura, cx.data_fechamento, f"R$ {cx.valor_inicial:.2f}", f"R$ {cx.valor_final:.2f if cx.valor_final is not None else 0:.2f}"] for cx in caixas]
        cabecalhos = ["ID", "Data Abertura", "Data Fechamento", "Valor Inicial", "Valor Final"]
        print(tabulate(tabela, headers=cabecalhos, tablefmt="grid", numalign="right", stralign="left"))
    else:
        print("Nenhum caixa aberto.")

def fechar_caixa(repo: CaixaRepo):
    """Função para lidar com a opção de fechar um caixa existente."""
    print("\n--- Fechamento de Caixa ---")
    try:
        caixa_id = obter_entrada_usuario("ID do caixa a ser fechado: ", int)
        caixa_existente = repo.obter(caixa_id)

        if caixa_existente:
            print("\nDados atuais do caixa:")
            print(f"  Data Abertura: {caixa_existente.data_abertura}")
            print(f"  Data Fechamento: {caixa_existente.data_fechamento}")
            print(f"  Valor Inicial: R$ {caixa_existente.valor_inicial:.2f}")
            print(f"  Valor Final: R$ {caixa_existente.valor_final:.2f if caixa_existente.valor_final is not None else 0:.2f}")
            print("\nDigite os novos dados (deixe em branco para manter o valor atual):")

            data_fechamento_str = obter_entrada_usuario(f"Nova Data Fechamento ({caixa_existente.data_fechamento}): ")
            data_fechamento = datetime.fromisoformat(data_fechamento_str) if data_fechamento_str else caixa_existente.data_fechamento

            valor_final_str = obter_entrada_usuario(f"Novo Valor Final: ")
            valor_final = float(valor_final_str) if valor_final_str else None

            caixa_atualizado = Caixa(id=caixa_existente.id, data_abertura=caixa_existente.data_abertura, data_fechamento=data_fechamento, valor_inicial=caixa_existente.valor_inicial, valor_final=valor_final)

            if repo.atualizar(caixa_atualizado):
                print(f"Caixa ID {caixa_id} fechado com sucesso!")
            else:
                print(f"Falha ao fechar o caixa ID {caixa_id}.")

        else:
            print(f"Caixa com ID {caixa_id} não encontrado.")

    except ValidationError as e:
        print("\nErro de validação ao fechar caixa:")
        for error in e.errors():
            print(f"- Campo '{error['loc'][0]}': {error['msg']}")
    except ValueError:
         print("Entrada inválida para ID, data ou valor. O fechamento foi cancelado.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao fechar o caixa: {e}")

def excluir_caixa(repo: CaixaRepo):
    """Função para lidar com a opção de excluir um caixa."""
    print("\n--- Exclusão de Caixa ---")
    try:
        caixa_id = obter_entrada_usuario("ID do caixa a ser excluído: ", int)

        caixa = repo.obter(caixa_id)
        if not caixa:
             print(f"Caixa com ID {caixa_id} não encontrado.")
             return

        confirmacao = input(f"Tem certeza que deseja excluir o caixa (ID: {caixa_id})? (s/N): ").lower()

        if confirmacao == 's':
            if repo.excluir(caixa_id):
                print(f"Caixa ID {caixa_id} excluído com sucesso.")
            else:
                print(f"Falha ao excluir o caixa ID {caixa_id}. Pode já ter sido removido.")
        else:
            print("Exclusão cancelada.")

    except ValueError:
         print("ID inválido. A exclusão foi cancelada.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao excluir: {e}")


import traceback

def main():
    """Função principal que executa o loop do menu interativo."""
    try:
        produto_repo = ProdutoRepo()
        comanda_repo = ComandaRepo()
        caixa_repo = CaixaRepo()

        while True:
            exibir_menu()
            opcao = input("Escolha uma opção: ").lower().strip()

            if opcao == 'a':
                cadastrar_produto(produto_repo)
            elif opcao == 'b':
                listar_produtos(produto_repo)
            elif opcao == 'c':
                alterar_produto(produto_repo)
            elif opcao == 'd':
                excluir_produto(produto_repo)
            elif opcao == 'e':
                cadastrar_comanda(comanda_repo)
            elif opcao == 'f':
                listar_comandas(comanda_repo)
            elif opcao == 'g':
                alterar_comanda(comanda_repo)
            elif opcao == 'h':
                excluir_comanda(comanda_repo)
            elif opcao == 'i':
                abrir_caixa(caixa_repo)
            elif opcao == 'j':
                listar_caixas(caixa_repo)
            elif opcao == 'k':
                fechar_caixa(caixa_repo)
            elif opcao == 'l':
                excluir_caixa(caixa_repo)
            elif opcao == 'm':
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

            input("\nPressione Enter para continuar...")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
