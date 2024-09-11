from models.funcionario import Funcionario
from models.endereco import Endereco
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa

endereco = Endereco("rua", "147", UnidadeFederativa.BAHIA)
funcionario = Funcionario(26, "Pedro", "07951235478", "20250324", "2121", "17/07/1998", Sexo.MASCULINO, Setor.JURIDICO, 5000, "33333333", "pedro@", endereco)

print(funcionario)