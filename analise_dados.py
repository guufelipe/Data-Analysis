import pandas as pd

dados = pd.read_csv('datasets/base_padronizada.csv', sep=';', decimal=',')

print(dados.head())

print(dados)


# Etapa 1 ->

contagem_aprovacao = dados['aprovado'].value_counts()   #contagem inteiro
percentuais_aprovacao = dados['aprovado'].value_counts(normalize=True) * 100 #contagem percentual


print("\nContagem de Aprovados/Reprovados:")
print('##############################################')
print(contagem_aprovacao)


print("\nPercentual de Aprovados/Reprovados:")
print('##############################################')
print(percentuais_aprovacao.round(2))


# Etapa 2 ->

resultado = pd.crosstab(dados['sexo'], dados['aprovado']) #Cruzar as colunas sexo e aprovado

# Exibir a tabela

print("\nContagem de Aprovados/Reprovados por Sexo")
print(resultado)
print('##############################################')

#Percentagem destas informações:
print("\nDistribuição por Sexo (Percentual em Relação ao Total Geral)")
percentual_coluna = pd.crosstab(dados['sexo'], dados['aprovado'], normalize='columns') * 100
print(percentual_coluna.round(2))
print('##############################################')


print('\nPercentual de Aprovação Dentro de Cada Sexo')
percentual_linha = pd.crosstab(dados['sexo'], dados['aprovado'], normalize='index') * 100
print(percentual_linha.round(2))
print('##############################################')


#Etapa 3 -> 
top5 = dados.sort_values(by='media', ascending=False).head(5)

print("\nTop 5 alunos com maiores médias:")
print(top5[['id_aluno', 'nome', 'media']])

print('##############################################')

#Etapa 4->

top5_frequencia = dados.sort_values(by='frequencia', ascending=False).head(5)


print("\nTop 5 alunos com maior frequência:")
print(top5_frequencia[['id_aluno', 'nome', 'frequencia']].reset_index(drop=True))
print('##############################################')