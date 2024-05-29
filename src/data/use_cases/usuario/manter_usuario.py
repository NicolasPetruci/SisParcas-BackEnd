from src.domain.models import Usuario
from src.domain.use_cases import ManterUsuarioInterface
from src.data.interfaces import UsuarioRepositoryInterface
from src.errors import HttpError
from typing import Dict, List

class ManterUsuario(ManterUsuarioInterface):

    @classmethod
    def __init__(self, repository: UsuarioRepositoryInterface):
        self.__repository = repository

    
    @classmethod
    def buscar_usuario_por_id(self, id: int) -> Dict:
        usuario = self.__repository.find_by_id(id)
        if usuario is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        return usuario.to_json()

    @classmethod
    def cadastrar(self, usuario: Usuario)->Dict:
        novo_usuario: Usuario = Usuario(
            None, 
            usuario.nome,
            usuario.email,
            usuario.telefone,
            usuario.senha,
            usuario.aniversario,
            usuario.id_cargo
            )
        return {
            "usuario": self.__repository.insert(novo_usuario).to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }
    

    @classmethod
    def buscar_usuarios(self) -> List[Dict]:
        usuarios: List[Usuario] = self.__repository.find_all()
        return list(c.to_json() for c in usuarios) 
    
    @classmethod
    def atualizar(self, usuario: Usuario) -> Dict:
        usuario_atualizado = self.__repository.update(usuario)
        if usuario_atualizado is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        return {
            "usuario": usuario_atualizado.to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }
    
    @classmethod
    def excluir(self, id: int) -> Dict: 
        usuario_excluido = self.__repository.delete_by_id(id)
        if usuario_excluido is None:
            raise HttpError(HttpError.error_404("Usuario não encontrado."))
        return {
            "usuario": usuario_excluido.to_json(),
            "message": "Usuario cadastrado com sucesso.",
        }