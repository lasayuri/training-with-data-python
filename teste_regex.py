import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"

#padrao = "[0-9][a-z]{2}[0-9]"
#texto = "123 1ax2 1cc aa1"

resposta = re.search(padrao, texto)
print(resposta.group())

#para encontrar email:
padraoEmail = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
textoEmail = "aaaabbbccc larissa123@gmail.com.br eailrjioewrjioew"
respostaEmail = re.search(padraoEmail, textoEmail)
print(respostaEmail.group())