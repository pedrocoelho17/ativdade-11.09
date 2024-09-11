from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Funcionario:
    def __init__(self, idade: int, nome: str, cpf: str, rg: str, matricula: str, dataNasc: str, sexo: Sexo, setor: Setor, salario: float, telefone: str, email: str, endereco: Endereco) -> None:
        self.idade = idade
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.dataNasc = dataNasc
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\nIdade: {self.idade}"
            f"\nNome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nData de nascimento: {self.dataNasc}"
            f"\nSexo: {self.sexo}"
            f"\nSetor: {self.setor}"
            f"\nSalário: {self.salario}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )    