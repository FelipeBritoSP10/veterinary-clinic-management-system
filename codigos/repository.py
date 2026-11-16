"""
Módulo de Repositório em Memória
Gerencia o armazenamento temporário de entidades no terminal.
"""
class ClinicaRepository:
    def __init__(self):
        self.veterinarios = []
        self.animais = []
        self.equipamentos = []
        self.prontuarios = []

    def adicionar_veterinario(self, vet):
        self.veterinarios.append(vet)

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def adicionar_equipamento(self, eq):
        self.equipamentos.append(eq)

    def adicionar_prontuario(self, pr):
        self.prontuarios.append(pr)
