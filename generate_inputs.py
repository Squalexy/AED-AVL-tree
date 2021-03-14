import random

doencas = ["doenca1", "doenca2", "doenca3", "doenca4", "doenca5", "doenca6", "doenca7", "doenca8", "doenca9",
           "doenca10"]
utentes = []
datas = []

for i in range(20):
    utentes.append(random.randint(0, 1000))

for i in range(30):
    dia = str(random.randint(0, 31))
    mes = str(random.randint(0, 12))
    ano = str(random.randint(2020, 2030))
    data = dia + "/" + mes + "/" + ano
    datas.append(data)


def generate_10ins_90con(num):
    ficheiro = "input_10ins_90con"
    with open(ficheiro + str(num) + ".in", 'w') as escrever:
        for k in range(num):
            doenca_random = random.randint(0, 9)
            utente_random = random.randint(0, 19)
            data_random = random.randint(0, 29)
            escrever.write(
                "ACRESCENTA" + " " + str(utentes[utente_random]) + " " + doencas[doenca_random] + " " + datas[
                    data_random] + "\n")
            for j in range(9):
                utente_random = random.randint(0, 19)
                escrever.write("CONSULTA" + " " + str(utentes[utente_random]) + "\n")


def generate_90ins_10con(num):
    ficheiro = "input_90ins_10cons"
    with open(ficheiro + str(num) + ".in", 'w') as escrever:
        for k in range(num):
            utente_random = random.randint(0, 19)
            escrever.write("CONSULTA" + " " + str(utentes[utente_random]) + "\n")
            for j in range(9):
                doenca_random = random.randint(0, 9)
                utente_random = random.randint(0, 19)
                data_random = random.randint(0, 29)
                escrever.write(
                    "ACRESCENTA" + " " + str(utentes[utente_random]) + " " + doencas[doenca_random] + " " + datas[
                        data_random] + "\n")


n = 1
for i in range(15):
    generate_10ins_90con(n)
    n += 1

n = 1
for i in range(15):
    generate_90ins_10con(n)
    n += 1
