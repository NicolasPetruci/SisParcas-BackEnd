from src.domain.models import Sessao
from src.domain.use_cases.sessao import ManterSessaoInterface
from src.data.interfaces import SessaoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterSessao(ManterSessaoInterface):

    @classmethod
    def __init__(self, repository: SessaoRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_sessao_por_id(self, id: int) -> Dict:
        sessao = self.__repository.find_by_id(id)
        if sessao is None:
            raise HttpError(HttpError.error_404("Sessao não encontrado."))
        return sessao.to_json()

    @classmethod
    def cadastrar(self, sessao: Sessao)->Dict:
        novo_sessao: Sessao = Sessao(
            None, 
            sessao.nome,
            sessao.descricao,
            sessao.data_hora,
            sessao.temporada,
            sessao.numero,
            sessao.rpg,
            []
            )
        return {
            "sessao": self.__repository.insert(novo_sessao).to_json(),
            "message": "Sessao cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_sessoes(self) -> List[Dict]:
        sessoes: List[Sessao] = self.__repository.find_all()
        return list(c.to_json() for c in sessoes) 
    
    @classmethod
    def atualizar(self, sessao: Sessao) -> Dict:
        sessao_atualizado = self.__repository.update(sessao)
        if sessao_atualizado is None:
            raise HttpError(HttpError.error_404("Sessao não encontrado."))
        return {
            "sessao": sessao_atualizado.to_json(),
            "message": "Sessao cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        sessao_excluido = self.__repository.delete_by_id(id)
        if sessao_excluido is None:
            raise HttpError(HttpError.error_404("Sessao não encontrado."))
        return {
            "sessao": sessao_excluido.to_json(),
            "message": "Sessao cadastrado com sucesso.",
        }