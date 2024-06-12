from src.domain.models import Mestre, Cargo, Usuario
from src.domain.use_cases.mestre import ManterMestreInterface
from src.data.interfaces import MestreRepositoryInterface
from src.errors import HttpError
from src.main.adapters.auth import encrypt_password
from typing import Dict, List

class ManterMestre(ManterMestreInterface):

    @classmethod
    def __init__(self, repository: MestreRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_mestre_por_id(self, id: int) -> Dict:
        mestre = self.__repository.find_by_id(id)
        if mestre is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        return mestre.to_json()

    @classmethod
    def buscar_mestre_por_id_usuario(self, id_usuario: int, cargos: List[Cargo]) -> Dict:
        mestre = self.__repository.find_by_id_usuario(id_usuario)
        if not mestre:
            if "MESTRE" not in cargos:
                raise HttpError(HttpError.error_401("Requisição requer cargo de mestre."))
            mestre = self.__repository.insert(Mestre(ativo=True, usuario=Usuario(id=request.payload.id)))
        return mestre.to_json()

    @classmethod
    def cadastrar(self, mestre: Mestre)->Dict:
        return {
            "mestre": self.__repository.insert(mestre).to_json(),
            "message": "Mestre cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_mestres(self) -> List[Dict]:
        mestres: List[Mestre] = self.__repository.find_all()
        return list(c.to_json() for c in mestres) 
    
    @classmethod
    def atualizar(self, mestre: Mestre) -> Dict:
        mestre_atualizado = self.__repository.update(mestre)
        if mestre_atualizado is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        return {
            "mestre": mestre_atualizado.to_json(),
            "message": "Mestre cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        mestre_excluido = self.__repository.delete_by_id(id)
        if mestre_excluido is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        return {
            "mestre": mestre_excluido.to_json(),
            "message": "Mestre cadastrado com sucesso.",
        }