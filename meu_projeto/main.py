from models.funcionario import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo

funcionario = Funcionario(26, "Pedro", 5000, Setor.FINANCEIRO, Sexo.MASCULINO)
print(funcionario)