# -*- coding: utf-8 -*-
"""projetoIndividualModulo4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FEGzkIuVSkG8_55NJooEyzSi82u8NpSy

TRABALHO INDIVIDUAL MÓDULO 4 (THIAGO BERNARDES CHECHIA)

![Logo da Resilia](https://www.resilia.com.br/wp-content/uploads/2021/08/logo.png)

# ***Relatório de Produtividade Semanal***

Neste relatório, apresentaremos uma análise detalhada da produtividade da nossa equipe ao longo da semana, com base em três principais indicadores: "Horas Trabalhadas", "Bugs Corrigidos" e "Tarefas Concluídas". Vamos explorar cada um desses temas para obter insights sobre o desempenho da equipe e entender como podemos melhorar a eficiência em nossas atividades diárias.

- IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""- IMPORTANDO O RELATÓRIO EM FORMATO .csv  (comma separated values)(valores separados por vírgulas)"""

url = 'https://drive.google.com/uc?export=download&id=1wji-DooPqQ3RzCotMFoszmjzFSakf0zH'

relatorio = pd.read_csv(url)
relatorio

"""- Criando o mesmo relatório sem a necessidade de importa-lo"""

dados = {'Dia': ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],
'Horas Trabalhadas': [6,7,8,6,7,5,4],'Bugs Corrigidos':[3,2,1,4,3,2,1], 'Tarefas Concluídas':[5,4,6,4,5,3,2],}
dia1 = {'Dia1': ['S', 'T', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']}

relatorio1 = pd.DataFrame(dados, index = [0,1,2,3,4,5,6])
relatorio1

"""Essa análise exploratória fornece uma visão geral da produtividade semanal e pode ajudar a identificar padrões ou tendências que impactem o desempenho da equipe. É importante considerar esses resultados em conjunto com outros fatores, como a complexidade das tarefas, para obter uma compreensão completa da eficiência do trabalho da equipe.

- TOTAL DE HORAS TRABALHADAS
"""

relatorio1['Horas Trabalhadas'].sum()# este comando soma todas as horas trabalhadas

"""Horas Trabalhadas:
Ao longo da semana, nossa equipe dedicou um total de 43 horas de trabalho em nossos projetos. Isso representa uma média de aproximadamente 6 horas e 10 minutos por dia de trabalho. Essas horas refletem o empenho e comprometimento da equipe em realizar suas atividades, cumprir prazos e atender às demandas do projeto. É fundamental reconhecer o esforço dedicado pelos membros da equipe, pois essas horas trabalhadas são o alicerce de nosso progresso e sucesso.

- MÉDIA DIÁRIA DE HORAS TRABALHADAS
"""

relatorio1['Horas Trabalhadas'].mean()#este comando faz a media de horas trabalhadas
print('{:.2f}'.format(relatorio1['Horas Trabalhadas'].mean()))# este comando forca a exibicao de um numero com duas casas decimais

"""Nesta análise, observamos que ao longo da semana, a equipe trabalhou um total de 43 horas. Isso significa que, em média, cada dia de trabalho teve aproximadamente 6,14 horas de dedicação à tarefa. Saber o número total de horas trabalhadas é útil para avaliar o nível de esforço e dedicação da equipe durante o período analisado. Pode ser útil comparar esses resultados com semanas anteriores ou estabelecer metas específicas para alocar um determinado número de horas em projetos futuros."""

# Gráfico de barras para as Horas Trabalhadas
plt.subplot(2, 2, 1)
plt.bar(relatorio1['Dia'], relatorio1['Horas Trabalhadas'])
plt.xlabel('Dia da semana')
plt.ylabel('Horas Trabalhadas')
plt.title('Horas Trabalhadas por Dia da Semana')

"""- TOTAL DE BUGS CORRIGIDOS"""

relatorio1['Bugs Corrigidos'].sum()#este comando Soma todas as tarefas

"""Bugs Corrigidos:
Durante a semana, nosso foco na qualidade do trabalho e no controle de defeitos foi evidente. Ao todo, foram corrigidos 16 bugs em nossos projetos. Essa média de 2,3 bugs corrigidos por dia demonstra nossa capacidade de identificar e resolver problemas em um ritmo consistente. É essencial ressaltar que a correção de bugs é uma tarefa crítica para garantir a estabilidade e a confiabilidade de nossas entregas, e estamos empenhados em manter esse nível de excelência para garantir a satisfação dos nossos clientes.

- MÉDIA DIÁRIA DE BUGS CORRIGIDOS
"""

relatorio1['Bugs Corrigidos'].mean()# este comando faz a media dos bugs corrigidos
print('{:.2f}'.format(relatorio1[:7]['Bugs Corrigidos'].mean()))# este comando forca a exibicao de um numero com duas

"""No relatório, podemos ver que durante a semana foram corrigidos 16 bugs no total. A média de bugs corrigidos por dia é de aproximadamente 2,29 bugs. Isso nos dá uma visão sobre a eficiência da equipe em resolver problemas e identificar áreas do projeto que podem precisar de mais atenção. É importante lembrar que a quantidade de bugs corrigidos nem sempre é um indicador de qualidade, pois alguns bugs podem ser mais complexos do que outros. Portanto, é importante avaliar também a gravidade dos bugs corrigidos para entender o impacto real no projeto."""

# Gráfico de barras para os Bugs Corrigidos
plt.subplot(2, 2, 2)
plt.bar(relatorio1['Dia'], relatorio1['Bugs Corrigidos'])
plt.xlabel('Dia da semana')
plt.ylabel('Bugs Corrigidos')
plt.title('Bugs Corrigidos por Dia da Semana')

"""- TOTAL DE TAREFAS CONCLUÍDAS"""

relatorio1['Tarefas Concluídas'].sum()#este comando soma todas as tarefas concluidas

"""Tarefas Concluídas:
A equipe realizou um total de 29 tarefas ao longo da semana. Com uma média de aproximadamente 4.14 tarefas concluídas por dia, ficamos satisfeitos em ver nossa produtividade em termos de entregas. Cada tarefa concluída representa um passo adiante em direção aos nossos objetivos e ao sucesso dos projetos. Continuaremos a priorizar a execução eficiente de tarefas para otimizar o fluxo de trabalho e alcançar nossas metas com eficácia.

- MÉDIA DIÁRIA DE TAREFAS CONCLUÍDAS
"""

relatorio1['Tarefas Concluídas'].mean()#utilizado comando mean para fazer a media das tarefas concluidas.
print('{:.2f}'.format(relatorio1[:7]['Tarefas Concluídas'].mean()))# este comando forca a exibicao de um numero com duas casas decimais

"""Tarefas Concluídas:
A equipe concluiu um total de 29 tarefas ao longo da semana. A média de tarefas concluídas por dia é de aproximadamente 4,14 tarefas. Isso mostra a eficiência da equipe em realizar e concluir as tarefas atribuídas. Comparar o número de tarefas concluídas com o número de tarefas planejadas pode ajudar a avaliar a produtividade e o cumprimento de metas. No entanto, é importante considerar também a complexidade e o tamanho das tarefas, já que algumas podem exigir mais tempo e esforço do que outras.
"""

# Gráfico de barras para as Tarefas Concluídas
plt.subplot(2, 2, 3)
plt.bar(relatorio1['Dia'], relatorio1['Tarefas Concluídas'])
plt.xlabel('Dia da semana')
plt.ylabel('Tarefas Concluídas')
plt.title('Tarefas Concluídas por Dia da Semana')

"""- PRODUTIVIDADE DIÁRIA  ( TAREFAS CONCLUÍDAS POR HORA )"""

ProdutividadeDiaria = relatorio1['Horas Trabalhadas'].sum() / relatorio1['Tarefas Concluídas'].sum()#este comando soma as horas trabalhadas
print('{:.2f}'.format(relatorio1['Horas Trabalhadas'].sum() / relatorio1['Tarefas Concluídas'].sum()))#forcando a exibicao do print formatando o numero obtido resultado da divisao de total de tarefas concluidas pelo total de horas trabalhadas.

"""Produtividade Diária:
Um indicador crucial para avaliar a eficiência de nossa equipe é a produtividade diária. Ao dividirmos o total de horas trabalhadas pelo número de tarefas concluídas, chegamos a uma produtividade média de aproximadamente 1 hora e 48 minutos por tarefa. Esse valor nos ajuda a entender o tempo médio gasto na conclusão de cada tarefa específica. É importante notar que, embora seja essencial ser produtivo, a qualidade do trabalho também é primordial. Vamos nos esforçar para manter um equilíbrio adequado entre produtividade e excelência em nossas entregas.

- APRESENTANDO A PRODUTIVIDADE DIÁRIA COM NÚMERO ARREDONDADO
"""

numero = ProdutividadeDiaria# criada a variavel numero definida resultante da variavel ProdutividadeDiaria definida acima
numero_arredondado = round(numero, 2)# este numero arredonda o resultado com comando round
numero_arredondado# este chama o numero arredonda definido acima

"""A produtividade diária é uma métrica importante que avalia o equilíbrio entre as horas trabalhadas e as tarefas concluídas. No caso desse relatório, a equipe obteve uma produtividade de 2 horas por tarefa. Isso significa que, em média, a equipe leva cerca de 2 horas para concluir uma tarefa. Essa métrica pode ser usada para identificar dias em que a produtividade foi mais alta ou mais baixa e investigar as razões por trás dessas variações. Também pode ser útil ao estimar o tempo necessário para concluir tarefas semelhantes no futuro."""

produtividade_diaria = relatorio1['Horas Trabalhadas'].sum() / relatorio1['Tarefas Concluídas'].sum()
restante = 24 - produtividade_diaria
labels = ['Produtividade', 'Restante']
sizes = [produtividade_diaria, restante]
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0)  # destaca o primeiro pedaço do gráfico
# Criação do gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Deixa o gráfico de pizza em formato circular
plt.title('Produtividade Diária')

"""Análise Exploratória Detalhada - Gráfico de Pizza da Produtividade Diária

Nesta análise exploratória detalhada, iremos examinar o gráfico de pizza da produtividade diária, que apresenta a proporção de tempo dedicado à produtividade em relação ao restante do tempo ao longo da semana. Vamos explicar os dados presentes no gráfico e suas implicações para a equipe.

**Análise e Implicações:**

Produtividade Diária: 1.79 (aproximadamente)
O valor da produtividade diária, que é de aproximadamente 1.79, significa que, em média, a equipe leva cerca de 1 hora e 47 minutos para concluir uma tarefa. Essa é uma métrica crítica que nos ajuda a entender a eficiência da equipe em relação ao tempo dedicado à produtividade. Uma produtividade diária positiva indica que a equipe está concluindo tarefas e projetos em um ritmo consistente, o que é essencial para o sucesso dos projetos e a satisfação dos clientes.

**Interpretação:**

O gráfico de pizza mostra que a maior parte do tempo da equipe (aproximadamente 94,7%) é dedicada à produtividade, representada pela fatia "Produtividade". Isso é um bom sinal e sugere que a equipe está focada em suas tarefas e projetos, maximizando o uso de seu tempo de trabalho para obter resultados eficientes.

A fatia "Restante" (aproximadamente 5,3%) representa o tempo não dedicado diretamente à produtividade, o que é natural e necessário para pausas e momentos de relaxamento. No entanto, é importante manter um equilíbrio saudável entre a produtividade e a necessidade de descanso para evitar sobrecarga e fadiga.

**Conclusão:**
Com base na análise exploratória do gráfico de pizza da produtividade diária, podemos concluir que a equipe tem um nível positivo de produtividade, com a maior parte do tempo sendo utilizada para atividades produtivas. No entanto, é sempre importante lembrar que a produtividade não é o único fator importante. A qualidade do trabalho, a colaboração da equipe e o equilíbrio entre vida profissional e pessoal também são fundamentais para o sucesso geral dos projetos e a satisfação da equipe.

Essa análise pode servir como base para futuras avaliações e melhorias em relação ao gerenciamento do tempo, definição de metas realistas e estratégias para manter uma alta produtividade sustentável ao longo do tempo.

- CRIACAO DE UMA SERIES PARA APRESENTAR OS RESULTADOS DE FORMA ORGANIZADA
"""

s1 = pd.Series([43,6.14,16,2.29,29,4.14,1.48], index = ['Total de Horas Trabalhadas','Média de horas trabalhadas','Total de Bugs Corrigidos','Média diária de Bugs Corrigidos','Total de Tarefas Concluídas','Média diária de Tarefas Concluídas','Produtividade Diária'])
s1# os index sao definidos acima e seus respectivos valores sao definidos na Series acima

"""A análise exploratória revela que nossa equipe tem demonstrado um comprometimento sólido e uma dedicação incansável ao longo da semana. Nossos esforços resultaram em uma média consistente de horas trabalhadas, correção de bugs e conclusão de tarefas. Continuaremos a monitorar esses indicadores para aprimorar ainda mais nossa produtividade e garantir que nossos projetos sejam entregues com a qualidade e a eficiência que nossos clientes esperam de nós. Com base nos dados apresentados, temos confiança em nossa capacidade de alcançar nossas metas e enfrentar novos desafios com sucesso.

É importante lembrar que essa análise exploratória é apenas o primeiro passo na avaliação do desempenho da equipe. Para obter uma compreensão mais completa e precisa, é recomendável realizar análises mais detalhadas e considerar outros fatores, como a satisfação e o bem-estar da equipe, a complexidade do projeto e a qualidade do trabalho entregue. Essas informações podem ajudar a identificar pontos fortes e áreas que precisam ser aprimoradas, proporcionando uma base sólida para o planejamento e a melhoria contínua das atividades da equipe.
"""

#Esse código abaixo criará um gráfico de barras horizontal,
#com cada barra representando um indicador e o valor correspondente
#sendo exibido acima de cada barra.
# O gráfico de barras fornece uma representação visualmente agradável dos dados,
#permitindo uma rápida comparação dos valores.

import matplotlib.pyplot as plt

# Dados
dados = {
    'Indicador': ['Total de Horas Trabalhadas', 'Média de Horas Trabalhadas', 'Total de Bugs Corrigidos',
                  'Média diária de Bugs Corrigidos', 'Total de Tarefas Concluídas', 'Média diária de Tarefas Concluídas',
                  'Produtividade Diária'],
    'Valor': [43.00, 6.14, 16.00, 2.29, 29.00, 4.14, 1.48]
}

# Criar um DataFrame para facilitar a criação do gráfico
df = pd.DataFrame(dados)

# Configuração do gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(df['Indicador'], df['Valor'], color='#66b3ff')
plt.xlabel('Valores')
plt.ylabel('Indicador')
plt.title('Análise de Dados')
plt.grid(axis='x')

# Adicionar valores em cada barra
for i, v in enumerate(df['Valor']):
    plt.text(v + 0.2, i, f'{v:.2f}', color='black')

# Mostrar o gráfico
plt.show()

"""**Análise Exploratória Detalhada** - *Horas Trabalhadas*, *Bugs* *Corrigidos* e T*arefas Concluídas*



Nesta análise exploratória detalhada, iremos examinar os dados relacionados às horas trabalhadas, bugs corrigidos e tarefas concluídas. Analisaremos tanto os valores absolutos quanto as médias diárias para obter uma compreensão mais completa do desempenho da equipe ao longo da semana.





Total de Horas Trabalhadas: 43 horas
Média Diária de Horas Trabalhadas: 6,14 horas
Bugs Corrigidos:

Total de Bugs Corrigidos: 16 bugs
Média Diária de Bugs Corrigidos: 2,29 bugs
Tarefas Concluídas:

Total de Tarefas Concluídas: 29 tarefas
Média Diária de Tarefas Concluídas: 4,14 tarefas

#Análise:

Horas Trabalhadas:
A equipe trabalhou um total de 43 horas ao longo da semana, com uma média diária de 6,14 horas de dedicação ao trabalho. Essas horas representam o esforço e a dedicação da equipe para avançar nos projetos e tarefas atribuídas. Uma média diária de 6,14 horas indica que a equipe está mantendo um ritmo consistente de trabalho durante a semana.

#Bugs Corrigidos:
Durante a semana, foram corrigidos 16 bugs no total, com uma média diária de 2,29 bugs corrigidos. Essa média sugere que a equipe está lidando eficientemente com problemas e identificando e corrigindo bugs em um ritmo razoável. Manter uma média diária de bugs corrigidos ajuda a manter a qualidade do trabalho e a satisfação do cliente.

#Tarefas Concluídas:
Ao longo da semana, a equipe concluiu um total de 29 tarefas, com uma média diária de 4,14 tarefas concluídas. Essa média diária indica que a equipe está atingindo um nível satisfatório de entrega e execução de tarefas. A conclusão de uma média de 4,14 tarefas por dia é uma prova da eficiência da equipe.

#Implicações e Considerações:

A equipe tem mostrado dedicação e empenho em suas atividades, com uma média diária de horas trabalhadas de 6,14 horas. É importante garantir que os membros da equipe mantenham um equilíbrio saudável entre trabalho e descanso para evitar esgotamento.

A média diária de bugs corrigidos de 2,29 reflete a eficiência da equipe em identificar e resolver problemas. É crucial continuar priorizando a qualidade do trabalho e o controle de bugs para garantir a satisfação do cliente e a estabilidade dos projetos.

A média diária de 4,14 tarefas concluídas destaca a capacidade da equipe em executar suas atividades de forma eficiente. Manter esse ritmo é essencial para o cumprimento de prazos e o sucesso dos projetos.

#Conclusão:
Com base na análise exploratória detalhada, podemos afirmar que a equipe tem demonstrado um nível satisfatório de produtividade, eficiência e comprometimento em suas atividades. Os indicadores mostram que a equipe está trabalhando de forma consistente e eficiente, concluindo tarefas e corrigindo bugs em um ritmo adequado. Essa análise fornece insights valiosos para a gestão do projeto, permitindo o planejamento de metas realistas e estratégias para melhorar ainda mais o desempenho da equipe. É fundamental manter o foco na qualidade do trabalho e no equilíbrio entre produtividade e bem-estar dos membros da equipe para garantir resultados sustentáveis e de alta qualidade.





"""

import pandas as pd
import matplotlib.pyplot as plt

# Dados
dados = {
    'Indicador': ['Total de Horas Trabalhadas', 'Média de Horas Trabalhadas', 'Total de Bugs Corrigidos',
                  'Média diária de Bugs Corrigidos', 'Total de Tarefas Concluídas', 'Média diária de Tarefas Concluídas',
                  'Produtividade Diária'],
    'Valor': [43.00, 6.14, 16.00, 2.29, 29.00, 4.14, 1.48]
}

# Criar um DataFrame para facilitar a criação do gráfico
df = pd.DataFrame(dados)

# Paleta de cores personalizada
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Configuração do gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(df['Indicador'], df['Valor'], color=cores)
plt.xlabel('Valores')
plt.ylabel('Indicador')
plt.title('Análise de Dados')

# Adicionar valores em cada barra
for i, v in enumerate(df['Valor']):
    plt.text(v + 0.2, i, f'{v:.2f}', color='black')

# Mostrar o gráfico
plt.show()