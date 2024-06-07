from src.domain.models import Genero
from src.domain.use_cases.genero import ManterGeneroInterface
from src.data.interfaces import GeneroRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterGenero(ManterGeneroInterface):

    @classmethod
    def __init__(self, repository: GeneroRepositoryInterface):
        self.__repository = repository

    @classmethod
    def buscar_genero_por_id(self, id: int) -> Dict:
        genero = self.__repository.find_by_id(id)
        if genero is None:
            raise HttpError(HttpError.error_404("Tipo de Evento não encontrado."))
        return genero.to_json()

    @classmethod
    def cadastrar(self, genero: Genero)->Dict:
        novo_genero: Genero = Genero(None, genero.descricao)
        return {
            "genero": self.__repository.insert(novo_genero).to_json(),
            "message": "Tipo de Evento cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_generos(self) -> List[Dict]:
        generos: List[Genero] = self.__repository.find_all()
        return list(g.to_json() for g in generos) 
    
    @classmethod
    def atualizar(self, genero: Genero) -> Dict:
        genero_atualizado = self.__repository.update(genero)
        if genero_atualizado is None:
            raise HttpError(HttpError.error_404("Genero não encontrado."))
        return {
            "genero": genero_atualizado.to_json(),
            "message": "Tipo de Evento atualizado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        genero_excluido = self.__repository.delete_by_id(id)
        if genero_excluido is None:
            raise HttpError(HttpError.error_404("Genero não encontrado."))
        return {
            "genero": genero_excluido.to_json(),
            "message": "Tipo de Evento excluído com sucesso.",
        }