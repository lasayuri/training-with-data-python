from cpf_cnpj import Cpf_Cnpj
from validate_docbr import CPF
from datas_br import DatasBr

# cpf_um = 12345678905
# objeto_cpf = Cpf_Cnpj(cpf_um)
# print(objeto_cpf)

cpf = "12345678905" #tem que ser string para passar pela formatação abaixo:
fatia_um = cpf[:3]
fatia_dois = cpf[3:6]
fatia_tres = cpf[6:9]
fatia_quatro = cpf[9:]
cpf_formatado = "{}.{}.{}-{}".format(
    fatia_um, fatia_dois, fatia_tres, fatia_quatro
)
print(cpf_formatado)

cpf_test = CPF()
print(cpf_test.validate("012.345.678-90"))

exemplo_cnpj = "35379838000112"
documento = Cpf_Cnpj(exemplo_cnpj, 'cnpj')
print(documento) 

cadastro = DatasBr()
print(cadastro.mes_cadastro())

 PEGAR MUDANÇAS GITHUB