from models.enums.setor import Setor
from models.enums.sexo import Sexo

class Funcionario:
    def __init__(self, idade: int, nome: str, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.idade = idade
        self.nome = nome
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
        

    def __str__(self) -> str:
        return(
            f"\nIdade: {self.idade}"
            f"\nNome: {self.nome}"
            f"\nSalário: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
        )    