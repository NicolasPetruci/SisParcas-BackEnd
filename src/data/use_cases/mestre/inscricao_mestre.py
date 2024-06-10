from src.domain.models import Mestre, Usuario, Cargo
from src.domain.use_cases.mestre import InscricaoMestreInterface
from src.data.interfaces import MestreRepositoryInterface, UsuarioRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class InscricaoMestre(InscricaoMestreInterface):

    @classmethod
    def __init__(
            self,
            repository: MestreRepositoryInterface,
            usuario_repository: UsuarioRepositoryInterface
            ):
        self.__repository = repository
        self.__usuario_repository = usuario_repository

    @classmethod
    def deferir(self, id_mestre: int) -> Dict:
        mestre: Mestre = self.__repository.find_by_id(id_mestre)
        if mestre is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        if mestre.ativo:
            raise HttpError(HttpError.error_400("Inscrição já foi deferida."))
        usuario: Usuario = self.__usuario_repository.find_by_id(mestre.usuario.id)
        usuario.cargos.append(Cargo(id = 3))
        self.__usuario_repository.update(usuario)
        mestre.set_ativo(True)
        mestre_atualizado = self.__repository.update(mestre)
        return {
            "mestre": mestre_atualizado.to_json(),
            "message": "Inscrição deferida com sucesso.",
        }
    
    @classmethod
    def indeferir(self, id_mestre: int) -> Dict:
        mestre: Mestre = self.__repository.find_by_id(id_mestre)
        if mestre is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        if not mestre.ativo:
            raise HttpError(HttpError.error_400("Inscrição já foi indeferida."))
        usuario: Usuario = self.__usuario_repository.find_by_id(mestre.usuario.id)
        usuario.cargos.remove(Cargo(id = 3))
        self.__usuario_repository.update(usuario)
        mestre.set_ativo(False)
        mestre_atualizado = self.__repository.update(mestre)
        return {
            "mestre": mestre_atualizado.to_json(),
            "message": "Inscrição indeferida com sucesso.",
        }