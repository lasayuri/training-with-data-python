from validate_docbr import CPF, CNPJ

class Cpf_Cnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido.")

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(self.cpf)
        else:
            return ValueError("Quantidade de dígitos inválida!")
    
    def format_cpf(self):
        # fatia_um = self.cpf[:3]
        # fatia_dois = self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:]
        # return(
        #     "{}.{}.{}-{}".format(
        #         fatia_um,
        #         fatia_dois,
        #         fatia_tres,
        #         fatia_quatro
        #     )
        # )
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            return ValueError("Quantidade de dígitos inválida!")