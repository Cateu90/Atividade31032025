from typing import List, Optional
from models.produto import Produto

class ProdutoRepo:
    def __init__(self):
        self.produtos = []
        self.next_id = 1

    def add_produto(self, produto: Produto) -> None:
        produto.id = self.next_id
        self.produtos.append(produto)
        self.next_id += 1

    def get_all_produtos(self) -> List[Produto]:
        return self.produtos

    def get_produto_by_id(self, id: int) -> Optional[Produto]:
        for produto in self.produtos:
            if produto.id == id:
                return produto
        return None

    def update_produto(self, produto: Produto) -> None:
        for index, p in enumerate(self.produtos):
            if p.id == produto.id:
                self.produtos[index] = produto
                break

    def delete_produto(self, id: int) -> None:
        self.produtos = [p for p in self.produtos if p.id != id]