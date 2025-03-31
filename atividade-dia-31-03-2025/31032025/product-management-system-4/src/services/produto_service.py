from pydantic import BaseModel
from typing import List, Optional
from src.models.produto import Produto
from src.repositories.produto_repo import ProdutoRepo

class ProdutoService:
    @staticmethod
    def add_produto(produto: Produto) -> None:
        ProdutoRepo.add_produto(produto)

    @staticmethod
    def get_all_produtos() -> List[Produto]:
        return ProdutoRepo.get_all_produtos()

    @staticmethod
    def get_produto_by_id(produto_id: int) -> Optional[Produto]:
        return ProdutoRepo.get_produto_by_id(produto_id)

    @staticmethod
    def update_produto(produto: Produto) -> None:
        ProdutoRepo.update_produto(produto)

    @staticmethod
    def delete_produto(produto_id: int) -> None:
        ProdutoRepo.delete_produto(produto_id)