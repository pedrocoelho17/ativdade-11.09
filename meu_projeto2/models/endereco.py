from models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, lagradouro: str, numero: str, uf: UnidadeFederativa) -> None:
        self.lagradouro = lagradouro
        self.numero = numero
        self.uf = uf

    def __str__(self) -> str:
        return(
            f"\nLagradouro: {self.lagradouro}"
            f"\nNúmero: {self.numero}"
            f"\nUnidade Federativa - nome: {self.uf.nome}"
            f"\nUnidade Federativa - sigla: {self.uf.sigla}"
        )    