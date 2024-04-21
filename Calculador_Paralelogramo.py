# Primeira proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos a multiplicação dos valores aprensentados
area = base * altura

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Segunda proposta de  Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = int(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = int(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos a multiplicação dos valores aprensentados
area = base * altura

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Terceira proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Retornamos para o usuário o resultado final passado em cm²
print('A Área do Paralelogramo:', base * altura, 'cm²')

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores com casas decimais

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quarta proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos a multiplicação dos valores aprensentados
area = base * altura

# Limitaremos as casas decimais para 2, aqui estamos arredondando o valor para 2 casas decimais
area_formatada = round(area, 2)

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quinta proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos a multiplicação dos valores aprensentados
area = base * altura

# Limitaremos as casas decimais para 2, aqui estamos formatando o valor para 2 casas decimais
area_formatada = '{:.2f}'.format(area)

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sexta proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos o arredondamento do resultado para 2 casas decimais
area = round(base * altura, 2)

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sétima proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos o arredondamento do resultado para 2 casas decimais
area = '{:.2f}'.format(base * altura)

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sétima proposta de Solução

# Iniciando o Calculador
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Realizamos a primeira pergunta para entender qual o comprimento da base do Paralelogramo 
base = float(input('Insira aqui o comprimento da base em cm: '))

# Realizamos a segunda pergunta para entender qual o comprimento da altura do Paralelogram
altura = float(input('Insira aqui o comprimento da altura em cm: '))

# Mostramos na tela o valor passado da base
print("Base:", base, "cm")

# Mostramos na tela o valor passado da base
print("Altura:", altura, "cm")

# Realizamos o arredondamento do resultado para 2 casas decimais
area = '{:.2f}'.format(base * altura)

# Retornamos para o usuário o resultado final passado em cm²
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Oitava proposta de Solução

# Bem-vindo e instruções
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Função para verificar se a entrada contém apenas números, caso contrario retornar para o usuário que seja inseridos apenas números
def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return float(entrada)
        else:
            print("Por favor, insira apenas números.")

# Solicitar e validar a entrada para a base
base = validar_entrada('Insira aqui o comprimento da base em cm: ')

# Solicitar e validar a entrada para a altura
altura = validar_entrada('Insira aqui o comprimento da altura em cm: ')

# Exibir os valores inseridos
print("Base:", base, "cm")
print("Altura:", altura, "cm")

# Calcular e exibir a área
area = base * altura
print("Área do Paralelogramo:", area, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nona Solução proposta de Solução

# Bem-vindo e instruções
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Função para verificar se a entrada contém apenas números, caso contrario retornar para o usuário que seja inseridos apenas números
def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return float(entrada)
        else:
            print("Por favor, insira apenas números.")

# Solicitar e validar a entrada para a base
base = validar_entrada('Insira aqui o comprimento da base em cm: ')

# Solicitar e validar a entrada para a altura
altura = validar_entrada('Insira aqui o comprimento da altura em cm: ')

# Exibir os valores inseridos
print("Base:", base, "cm")
print("Altura:", altura, "cm")

# Calcular e exibir a área
area = base * altura

# Arredonda a area total para 2 casas decimais
area_formatada = round(area, 2)

print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Décima Solução proposta de Solução

# Bem-vindo e instruções
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Função para verificar se a entrada contém apenas números, caso contrario retornar para o usuário que seja inseridos apenas números
def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return float(entrada)
        else:
            print("Por favor, insira apenas números.")

# Solicitar e validar a entrada para a base
base = validar_entrada('Insira aqui o comprimento da base em cm: ')

# Solicitar e validar a entrada para a altura
altura = validar_entrada('Insira aqui o comprimento da altura em cm: ')

# Exibir os valores inseridos
print("Base:", base, "cm")
print("Altura:", altura, "cm")

# Calcular e exibir a área
area = base * altura

# Arredonda a area total para 2 casas decimais
area_formatada = '{:.2f}'.format(area)

print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Décima Primeira Solução proposta de Solução

# Bem-vindo e instruções
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Valindando a entrada para que seja inseridos apenas números tanto com casas decimais ou não, caso contrario retornar para o usuário que seja inseridos apenas números
def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print("Por favor, insira apenas números.")

# Solicitar e validar a entrada para a base
base = validar_entrada('Insira aqui o comprimento da base em cm: ')

# Solicitar e validar a entrada para a altura
altura = validar_entrada('Insira aqui o comprimento da altura em cm: ')

# Exibir os valores inseridos
print("Base:", base, "cm")
print("Altura:", altura, "cm")

# Calcular e exibir a área
area = base * altura

# Arredonda a area total para 2 casas decimais
area_formatada = '{:.2f}'.format(area)

print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Décima Segunda Solução proposta de Solução

# Bem-vindo e instruções
print('Bem-vindo ao Calculador de Área de Paralelogramo')

# Valindando a entrada para que seja inseridos apenas números tanto com casas decimais ou não, caso contrario retornar para o usuário que seja inseridos apenas números
def validar_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            print("Por favor, insira apenas números.")

# Solicitar e validar a entrada para a base
base = validar_entrada('Insira aqui o comprimento da base em cm: ')

# Solicitar e validar a entrada para a altura
altura = validar_entrada('Insira aqui o comprimento da altura em cm: ')

# Exibir os valores inseridos
print("Base:", base, "cm")
print("Altura:", altura, "cm")

# Calcular e exibir a área
area = base * altura

# Arredonda a area total para 2 casas decimais
area_formatada = round(area, 2)

print("Área do Paralelogramo:", area_formatada, "cm²")

# Atenção! DEVIDO A FUNÇÃO INPUT TRAZER COMO RESULTADO UMA STRING, QUANDO QUEREMOS QUE O RESULTADO SEJA EM NUMERO, TEMOS QUE USAR OU INT(), OU FLOAT()
# INT() = apenas para números inteiros
# FLOAT() = para valores flutuantes