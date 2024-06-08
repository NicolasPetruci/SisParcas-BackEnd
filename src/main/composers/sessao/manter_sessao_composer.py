from src.data.use_cases.sessao import ManterSessao
from src.infra.db.repositories import SessaoRepository
from src.presentation.controller.sessao import ManterSessaoController

def compose_methods():
    repository = SessaoRepository()
    use_case = ManterSessao(repository)
    controller = ManterSessaoController(use_case)

    return controller


def atualizar_sessao_composer():
    controller = compose_methods()
    return controller.atualizar

def buscar_sessoes_composer():
    controller = compose_methods()
    return controller.buscar

def buscar_sessao_por_id_composer():
    controller = compose_methods()
    return controller.buscar_por_id

def excluir_sessao_composer():
    controller = compose_methods()
    return controller.excluir

def cadastrar_sessao_composer():
    controller = compose_methods()
    return controller.cadastrar

def atualizar_sessao_composer():
    controller = compose_methods()
    return controller.atualizar