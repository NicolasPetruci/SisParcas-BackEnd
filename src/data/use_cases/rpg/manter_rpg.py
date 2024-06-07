from src.domain.models import RPG
from src.domain.use_cases.rpg import ManterRPGInterface
from src.data.interfaces import RPGRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterRPG(ManterRPGInterface):

    @classmethod
    def __init__(self, repository: RPGRepositoryInterface):
        self.__repository = repository

    @classmethod
    def buscar_rpg_por_id(self, id: int) -> Dict:
        rpg = self.__repository.find_by_id(id)
        if rpg is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        return rpg.to_json()

    @classmethod
    def cadastrar(self, rpg: RPG)->Dict:
        novo_rpg: RPG = RPG(
            None, 
            rpg.nome,
            rpg.descricao,
            rpg.mestre,
            generos = rpg.generos,
            )
        return {
            "rpg": self.__repository.insert(novo_rpg).to_json(),
            "message": "RPG cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_rpgs(self) -> List[Dict]:
        rpgs: List[RPG] = self.__repository.find_all()
        return list(c.to_json() for c in rpgs) 
    
    @classmethod
    def atualizar(self, rpg: RPG) -> Dict:
        rpg_atualizado = self.__repository.update(rpg)
        if rpg_atualizado is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        return {
            "rpg": rpg_atualizado.to_json(),
            "message": "RPG cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        rpg_excluido = self.__repository.delete_by_id(id)
        if rpg_excluido is None:
            raise HttpError(HttpError.error_404("RPG não encontrado."))
        return {
            "rpg": rpg_excluido.to_json(),
            "message": "RPG cadastrado com sucesso.",
        }