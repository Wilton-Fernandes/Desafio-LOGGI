# Nome: Wilton Fernandes Landim
# Universidade: Faculdade Impacta de Tecnologia
# Curso: Análise e Desenvolvimento de Sistemas
# 2° Semestre
# Conclusão: 12/2023


from typing import Counter

# Os pacotes do desafio foram colocados em forma de dicionario.
pacotes = {'Pacote 1':'288355555123888', 
           'Pacote 2':'335333555584333', 
           'Pacote 3':'223343555124001', 
           'Pacote 4':'002111555874555', 
           'Pacote 5':'111188555654777', 
           'Pacote 6':'111333555123333', 
           'Pacote 7':'432055555123888', 
           'Pacote 8':'079333555584333', 
           'Pacote 9':'155333555124001', 
           'Pacote 10':'333188555584333', 
           'Pacote 11':'555288555123001', 
           'Pacote 12':'111388555123555', 
           'Pacote 13':'288000555367333', 
           'Pacote 14':'066311555874001', 
           'Pacote 15':'110333555123555', 
           'Pacote 16':'333488555584333', 
           'Pacote 17':'455448555123001', 
           'Pacote 18':'022388555123555', 
           'Pacote 19':'432044555845333', 
           'Pacote 20':'034311555874001'}

############################################# FUNCÕES ###########################################################################
# Função que define a região de origem
def regiao_origem(pacote):
    cidade = int(pacote[0:3])

    if cidade >= 1 and cidade <100:
        regiao = 'Região Sudeste'
    elif cidade >= 100 and cidade <200:
        regiao = 'Região Sul'
    elif cidade > 200 and cidade <300:
        regiao ='Região Centro-oeste'
    elif cidade >= 300 and cidade <400:
        regiao ='Região Nordeste'
    elif cidade >= 400 and cidade <500:
        regiao ='Região Norte'
    else:
        regiao ='Região Inválida'
    return regiao

# Função que define a região de destino
def regiao_destino(pacote):
    cidade = int(pacote[3:6])

    if cidade >= 1 and cidade <100:
        regiao = 'Região Sudeste'
    elif cidade >= 100 and cidade <200:
        regiao = 'Região Sul'
    elif cidade >= 200 and cidade <300:
        regiao ='Região Centro-oeste'
    elif cidade >= 300 and cidade <400:
        regiao ='Região Nordeste'
    elif cidade >= 400 and cidade <500:
        regiao ='Região Norte'
    else:
        regiao ='Região Inválida'
    return regiao

# Função que define o tipo do produto
def tipo(codigo):
    if codigo[12:15] == '001':
        return ('Jóias')
    elif codigo[12:15] == '111':
        return ('Livros')
    elif codigo[12:15] == '333':
        return ('Eletrônicos')
    elif codigo[12:15] == '555':
        return ('Bebidas')
    elif codigo[12:15] == '888':
        return ('Brinquedos')

# Função que imprime um separador de questões em forma de linha
def cabecalho():
    return (print('______________________________________________________________________________________________________________'),
            print(''))

################################################ Validação dos códigos ############################################################

codigos_validos = {}
codigos_invalidos = {}

for pacote, codigo in pacotes.items():
    # Confere se código tem 15 algarismos
    if len(codigo) != 15:
        codigos_invalidos[pacote] = codigo 
    # Confere se o código é o 555 referente a LOGGI
    elif int(codigo[6:9]) != 555:
        codigos_invalidos[pacote] = codigo
    #Confere se os pacotes possuem códigos de região inválidos
    elif  int(codigo[0:3]) > 499 or int(codigo[0:3]) == 200 or int(codigo[3:6]) > 499 or int(codigo[3:6]) == 200:
        codigos_invalidos[pacote] = codigo
    #Confere se os pacotes possuem códigos de tipo de produtos inválidos
    elif codigo[12:15] != '001' and codigo[12:15] != '111' and codigo[12:15] != '333' and codigo[12:15] != '555' and codigo[12:15] != '888':
        codigos_invalidos[pacote] = codigo
    #Restringe despachar jóias de pacotes com origem da região Centro-oeste
    elif codigo[12:15] == '001' and regiao_origem(codigo) == 'Região Centro-oeste':
        codigos_invalidos[pacote] = codigo
    #Restringe vendedor 367 por CNPJ inválido
    elif codigo[9:12] == '367':
        codigos_invalidos[pacote] = codigo
    else:
        codigos_validos[pacote] = codigo

####################################################### Questão 1 ################################################################

cabecalho()
print('1 - Identificar a região de destino de cada pacote, com totalização de pacotes (soma região);')
print('OBSERVAÇÃO: FOI CONSIDERADO TODOS PACOTES, SEM RETIRAR OS INVÁLIDOS')
cabecalho()
sul = 0
norte = 0
centro_oeste = 0
nordeste = 0
sudeste = 0
invalido = 0


for pacote, codigo in pacotes.items():
    b = regiao_destino(codigo)
    if b == 'Região Sudeste':
        print(f'{pacote}: Região Sudeste')
        
        sudeste+=1
    elif b == 'Região Sul':
        print(f'{pacote}: Região Sul')
        sul+=1
    elif b == 'Região Centro-oeste':
        print(f'{pacote}: Região Centro-oeste')
        centro_oeste+=1
    elif b == 'Região Nordeste':
        print(f'{pacote}: Região Nordeste')
        nordeste+=1
    elif b == 'Região Norte':
        print(f'{pacote}: Norte')
        norte+=1
    else:
        print(f'{pacote}: Região Inválida')
        invalido+=1
    

print('')
print('Total Região Centro-oeste: ', centro_oeste)
print('Total Região Nordeste: ', nordeste)
print('Total Região Norte: ', norte)
print('Total Região Sudeste: ', sudeste)
print('Total Região Sul: ', sul)
print('Total Região Inválida: ', invalido)

######################################################## Questão 2 #################################################################
cabecalho()
print('2- Saber quais pacotes possuem códigos de barras válidos e/ou inválidos;')
cabecalho()

print('Pacotes Válidos:')
for pacote, codigo in codigos_validos.items():
    print(f'{pacote}: {codigo}')
print('')
print('Pacotes Inválidos:')
for pacote, codigo in codigos_invalidos.items():
    print(f'{pacote}: {codigo}')

######################################################## Questão 3 #################################################################
cabecalho()
print('3- Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo;')
cabecalho()

numero = 0
for pacote, codigo in codigos_validos.items():
    if regiao_origem(codigo) == 'Região Sul' and codigo[12:15] == '888':
        print(f'{pacote}:{codigo}')
        numero+=1
if numero == 0:
    print('Sem pacotes com estas caracteristicas')

######################################################## Questão 4 #################################################################
cabecalho()       
print('4- Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos);')
cabecalho()

print('Pacotes com destino a região Sudeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Sudeste':
        print(f'{pacote}:{codigo}')

print('')
print('Pacotes com destino a região Sul:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Sul':
        print(f'{pacote}:{codigo}')

print('')
print('Pacotes com destino a região Centro-oeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste':
        print(f'{pacote}:{codigo}')

print('')
print('Pacotes com destino a região Nordeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste':
        print(f'{pacote}:{codigo}')

print('')
print('Pacotes com destino a região Norte:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte':
        print(f'{pacote}:{codigo}')

######################################################### Questão 5 ###############################################################
cabecalho()
print('5- Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos);')
cabecalho()

lista_vendedores = []
for pacote, codigo in codigos_validos.items():
    lista_vendedores.append(codigo[9:12])
c = Counter(lista_vendedores)
for vendedor, qtd in c.items():
    print(f'O vendedor {vendedor} enviou {qtd} pacotes')

######################################################### Questão 6 ###############################################################
cabecalho()
print('6- Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos);')
cabecalho()

print('Pacotes com destino a região Sudeste:')

for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Sudeste':
        print(f'{pacote}: {tipo(codigo)}')

print('')
print('Pacotes com destino a região Sul:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Sul':
        print(f'{pacote}: {tipo(codigo)}')

print('')
print('Pacotes com destino a região Centro-oeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste':
        print(f'{pacote}: {tipo(codigo)}')

print('')
print('Pacotes com destino a região Nordeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste':
        print(f'{pacote}: {tipo(codigo)}')

print('')
print('Pacotes com destino a região Norte:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte':
        print(f'{pacote}: {tipo(codigo)}')

######################################################### Questão 7 ##################################################################
cabecalho()
print('7- Se o transporte dos pacotes para o Norte passa pela Região Centro-Oeste, quais são os pacotes \
que devem ser despachados no mesmo caminhão? Gerar o relatório/lista de pacotes por destino e por tipo \
(Considere apenas pacotes válidos);')
cabecalho()

print('* Se o caminhão passa pelo Centro-oeste e vai em direção ao Norte, então a rota seria Centro-oste > Nordeste > Norte, nesta ordem.')
print('')
print('Pacotes com destino a região Centro-oeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

print('')
print('Pacotes com destino a região Nordeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

print('')
print('Pacotes com destino a região Norte:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

########################################################## Questão 8 #############################################################
cabecalho()
print('8- Se todos os pacotes fossem uma fila qual seria a ordem de carga para o Norte no caminhão para descarregar os pacotes da Região\
Centro Oeste primeiro;')
cabecalho()

print('* Neste caso, o caminhão deve ser carregado nesta ordem: Norte > Nordeste > Centro-oeste')

print('')
print('Pacotes com destino a região Norte:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

print('')
print('Pacotes com destino a região Nordeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

print('')
print('Pacotes com destino a região Centro-oeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

########################################################### Questão 9 ############################################################
cabecalho()
print('9- No item acima considerar que as jóias fossem sempre as primeiras a serem descarregadas;')
cabecalho()

print('* Neste caso, carregar o caminhão sempre por ultimo as jóias em cada região')
print('')

print('Pacotes com destino a região Norte:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte' and tipo(codigo) != 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Norte' and tipo(codigo) == 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')


print('')
print('Pacotes com destino a região Nordeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste' and tipo(codigo) != 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Nordeste' and tipo(codigo) == 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

print('')
print('Pacotes com destino a região Centro-oeste:')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste' and tipo(codigo) != 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')
for pacote, codigo in codigos_validos.items():
    if regiao_destino(codigo) == 'Região Centro-oeste' and tipo(codigo) == 'Jóias':
        print(f'{pacote}:{codigo} - {tipo(codigo)}')

########################################################### Questão 10 ###########################################################
cabecalho()
print('10- Listar os pacotes inválidos.')
cabecalho()

print('Pacotes Inválidos:')
for pacote, codigo in codigos_invalidos.items():
    print(f'{pacote}: {codigo}')
print('')