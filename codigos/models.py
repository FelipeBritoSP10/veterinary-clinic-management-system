"""
Módulo de Modelos de Domínio - Clínica Veterinária
Implementa Herança, Encapsulamento, Polimorfismo, Composição e Associação.
"""
from abc import ABC, abstractmethod
from typing import List


class Pessoa:
    def __init__(self, nome: str, telefone: str):
        self._nome = nome
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def telefone(self) -> str:
        return self._telefone


class Veterinario(Pessoa):
    def __init__(self, nome: str, telefone: str, crmv: str, especialidade: str):
        super().__init__(nome, telefone)
        self.crmv = crmv
        self.especialidade = especialidade

    @property
    def crmv(self) -> str:
        return self._crmv

    @crmv.setter
    def crmv(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            raise ValueError("O CRMV não pode ser nulo ou vazio.")
        self._crmv = valor

    def realizar_atendimento(self, animal: 'Animal') -> str:
        return f"Dr(a). {self.nome} (CRMV: {self.crmv}) iniciou o atendimento do paciente: {animal.nome}."


class Animal:
    def __init__(self, nome: str, especie: str, idade: int):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def get_info(self) -> str:
        return f"{self.nome} ({self.especie}, {self.idade} anos)"


class Equipamento:
    def __init__(self, nome: str, status_operacional: str):
        self.nome = nome
        self.status_operacional = status_operacional

    def verificar_status(self) -> str:
        return f"Equipamento '{self.nome}': Status [{self.status_operacional}]."


class Exame(ABC):
    def __init__(self, descricao: str, valor_base: float):
        self.descricao = descricao
        self.valor_base = valor_base

    @abstractmethod
    def executar(self) -> float:
        pass


class ExameLaboratorial(Exame):
    def __init__(self, descricao: str, valor_base: float, taxa_reagente: float):
        super().__init__(descricao, valor_base)
        self.taxa_reagente = taxa_reagente

    def executar(self) -> float:
        custo_total = self.valor_base + self.taxa_reagente
        print(f"  [Exame Laboratorial] {self.descricao} -> Base: R$ {self.valor_base:.2f} + Reagente: R$ {self.taxa_reagente:.2f} = R$ {custo_total:.2f}")
        return custo_total


class ExameImagem(Exame):
    def __init__(self, descricao: str, valor_base: float, taxa_equipamento: float):
        super().__init__(descricao, valor_base)
        self.taxa_equipamento = taxa_equipamento

    def executar(self) -> float:
        custo_total = self.valor_base + self.taxa_equipamento
        print(f"  [Exame de Imagem] {self.descricao} -> Base: R$ {self.valor_base:.2f} + Equipamento: R$ {self.taxa_equipamento:.2f} = R$ {custo_total:.2f}")
        return custo_total


class Prontuario:
    def __init__(self, codigo: str, animal: Animal, veterinario: Veterinario):
        self._codigo = codigo
        self.animal = animal
        self.veterinario = veterinario
        self._exames: List[Exame] = []

    @property
    def codigo(self) -> str:
        return self._codigo

    def adicionar_exame(self, exame: Exame):
        self._exames.append(exame)

    def calcular_custo_total(self) -> float:
        print(f"--- Processando Exames do Prontuário [{self.codigo}] ---")
        return sum(exame.executar() for exame in self._exames)
