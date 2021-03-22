import json


def lerarquivo(nome):
    with open(nome, 'r', encoding='utf-8') as json_file:
        dados = json.load(json_file)

    return dados


def checaRegras(automato):
    regras = automato["regras"]
    alfabeto = automato["alfabeto"]

    for chave in regras:
        for chave_estado in regras[chave]:
            if chave_estado not in alfabeto:
                return False

    return True


def checaCadeiaValida(cadeia, automato):
    if not checaRegras(automato):
        return False

    regras = automato["regras"]
    estadoAtual = automato["inicio"]

    for caracter in cadeia:
        if caracter in regras[estadoAtual]:
            estadoAtual = regras[estadoAtual][caracter]
        else:
            return False

    return estadoAtual in automato["final"]


automato = lerarquivo("automato.json")
cadeias = lerarquivo("cadeias.json")

for cadeia in cadeias:
    if checaCadeiaValida(cadeia, automato):
        print(f"A cadeia {cadeia} é válida!")
    else:
        print(f"A cadeia {cadeia} não é válida!")
