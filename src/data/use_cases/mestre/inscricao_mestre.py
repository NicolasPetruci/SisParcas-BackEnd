from src.domain.models import Mestre
from src.domain.use_cases.mestre import InscricaoMestreInterface
from src.data.interfaces import MestreRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class InscricaoMestre(InscricaoMestreInterface):

    @classmethod
    def __init__(
            self,
            repository: MestreRepositoryInterface
            ):
        self.__repository = repository

    @classmethod
    def deferir(self, id_mestre: int) -> Dict:
        mestre: Mestre = self.__repository.find_by_id(id_mestre)
        if mestre is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        if mestre.ativo:
            raise HttpError(HttpError.error_404("Inscrição já foi deferida."))
        mestre.set_ativo(True)
        mestre_atualizado = self.__repository.update(mestre)
        return {
            "mestre": mestre_atualizado.to_json(),
            "message": "Inscrição deferida com sucesso.",
        }
    
    def indeferir(self, id_mestre: int) -> Dict:
        mestre: Mestre = self.__repository.find_by_id(id_mestre)
        if mestre is None:
            raise HttpError(HttpError.error_404("Mestre não encontrado."))
        if not mestre.ativo:
            raise HttpError(HttpError.error_404("Inscrição já foi indeferida."))
        mestre.set_ativo(False)
        mestre_atualizado = self.__repository.update(mestre)
        return {
            "mestre": mestre_atualizado.to_json(),
            "message": "Inscrição indeferida com sucesso.",
        }