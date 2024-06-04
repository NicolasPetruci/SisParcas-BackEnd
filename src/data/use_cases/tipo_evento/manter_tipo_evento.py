from src.domain.models import TipoEvento
from src.domain.use_cases.tipo_evento import ManterTipoEventoInterface
from src.data.interfaces import TipoEventoRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterTipoEvento(ManterTipoEventoInterface):

    @classmethod
    def __init__(self, repository: TipoEventoRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_tipo_evento_por_id(self, id: int) -> Dict:
        tipo_evento = self.__repository.find_by_id(id)
        if tipo_evento is None:
            raise HttpError(HttpError.error_404("Tipo de Evento não encontrado."))
        return tipo_evento.to_json()

    @classmethod
    def cadastrar(self, tipo_evento: TipoEvento)->Dict:
        novo_tipo_evento: TipoEvento = TipoEvento(None, tipo_evento.descricao)
        return {
            "tipo_evento": self.__repository.insert(novo_tipo_evento).to_json(),
            "message": "Tipo de Evento cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_tipo_eventos(self) -> List[Dict]:
        tipo_eventos: List[TipoEvento] = self.__repository.find_all()
        return list(c.to_json() for c in tipo_eventos) 
    
    @classmethod
    def atualizar(self, tipo_evento: TipoEvento) -> Dict:
        tipo_evento_atualizado = self.__repository.update(tipo_evento)
        if tipo_evento_atualizado is None:
            raise HttpError(HttpError.error_404("TipoEvento não encontrado."))
        return {
            "tipo_evento": tipo_evento_atualizado.to_json(),
            "message": "Tipo de Evento atualizado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        tipo_evento_excluido = self.__repository.delete_by_id(id)
        if tipo_evento_excluido is None:
            raise HttpError(HttpError.error_404("TipoEvento não encontrado."))
        return {
            "tipo_evento": tipo_evento_excluido.to_json(),
            "message": "Tipo de Evento excluído com sucesso.",
        }