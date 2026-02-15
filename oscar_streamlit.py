import pandas as pd
import streamlit as st


st.header("Análise de Dados | Passo a Passo", divider=True)

st.write("Este projeto..... Confira na página principal.")

st.subheader("1. Entendendo os dados e suas limitações", divider="gray")

st.markdown("""O primeiro passo é abrir os conjuntos de dados.

Na base de dados utilizada, temos dois arquivos:

- `full_data.csv`:
- `the_oscar_award.csv`:
""")

st.write("Vamos começar abrindo o arquivo `full_data.csv` pelo OnlyOffice antes de abrir pelo Pandas. O programa irá nos informar algumas coisas interessantes, a começar pela formatação dos dados:")


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("fulldata_onlyoffice.png", caption="Abrindo o arquivo `full_data.csv` pelo OnlyOffice.")

st.markdown("""Há algumas coisas interessantes a se apontar sobre este procedimento:

- :red[Limitações de programa:] este procedimento **NÃO** é útil para bases de dados muito grandes, que exigem maior poder de processamento para sequer carregar no seu programa de planilha comparados a uma operação direta pelo Pandas/Python;
- :red[Amplitude de conteúdo]: apesar do Pandas conter funções como `head()`, `tail()` ou `sample()` para procurar por linhas da tabela, utilizando um programa de planilha se tem uma praticidade muito maior de analisar os dados de um número muito maior de colunas.""")

st.write("Agora abriremos o mesmo arquivo pelo Pandas utilizando a referência que nos foi dada:")

st.code("""import pandas as pd
df = pd.read_csv("full_data.csv", encoding="utf-8", sep="\ t")""", language="python")


df = pd.read_csv("full_data.csv", encoding="utf-8", sep='\t')

st.write(f"Número de linhas e colunas: `{df.shape}`")
st.dataframe(df, hide_index=True)


st.write("Utilizando o método `describe`:")
df_describe = df.describe(include='all').fillna("").astype("str")
st.write(df_describe)



st.write("Faremos o mesmo procedimento para o arquivo `the_oscar_award.csv`, para checar as diferenças entre as duas bases de dados:")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("the_oscar_award_onlyoffice.png", caption="Abrindo o arquivo `the_oscar_award.csv` pelo OnlyOffice.")

st.code("""import pandas as pd
df = pd.read_csv("the_oscar_award.csv", encoding="utf-8", sep=",")""", language="python")

df2 = pd.read_csv("the_oscar_award.csv", encoding="utf-8", sep=',')

st.write(f"Número de linhas e colunas: `{df2.shape}`")
st.dataframe(df2, hide_index=True)

st.write("Utilizando o método `describe`:")
df2_describe = df2.describe(include='all').fillna("").astype("str")
st.write(df2_describe)


st.html("""<h2>Conclusão da análise prévia dos dados</h2>
Podemos, a partir disso, coletar algumas informações importantes e já tomar algumas decisões de acordo com algumas colunas:""")

st.write("""
| Coluna | Ajuste |
| --- | --- |
| `Year` | A coluna no arquivo `full_data.csv` não possui uma formatação correta de data para o Pandas, somente indicando a referência de qual evento do Oscar se tratou. |
| `name` e `film` | O arquivo `full_data.csv` possui mais nomes de indicados e de filmes presentes do que `the_oscar_award.csv`. Isso precisará ser analisado para entender e padronizar as informações entre as duas tabelas. Além disso, há dados vazios nestas colunas em ambas bases de dados. |
| `name` | As indicações que possuem mais de uma pessoa participando estão quebradas com `,` ou `/` nas tabelas. Em caso de alguma análise baseada em nome, isso precisará ser ajustado. |
| `note` | Algumas informações que podem ter grande relevância para alguns dos conflitos com as colunas `name` e `film` estão descritos nesta coluna. |
""")

# Parte 2 - Tratando os dados da planilha
st.subheader("2. Tratando os dados da planilha", divider="gray")

st.write("""Vamos começar tentando padronizar os dados das colunas `year` e `film`. O objetivo é termos o mesmo número de linhas entre as duas bases após removermos os valores vazios e outras alterações.

Para isso, fazemos:""")

st.code('''df.dropna(axis=0, subset=["Name", "Film"]).reset_index(drop=True)''')

df_limpo = df.dropna(axis=0, subset=["Name", "Film"]).reset_index(drop=True)

st.write(f"Verificando o número de linhas/colunas de `df`: `{df_limpo.shape}`")
st.dataframe(df_limpo)

df2_limpo = df2.dropna(axis=0, subset=["name", "film"]).reset_index(drop=True)

st.write(f"Verificando o número de linhas/colunas de `df2`: `{df2_limpo.shape}`")
st.dataframe(df2_limpo)

st.write("Podemos perceber que em `df2` há 36 linhas a mais. Vamos investigar aonde ocorrem essas inconsistências:")

st.write("Analisando `df`")
st.dataframe(df_limpo.value_counts("Year").reset_index().sort_values(by="Year", ascending=True).head())

st.write("Analisando `df2`")
st.dataframe(df2_limpo.value_counts("year_film").reset_index().sort_values(by="year_film", ascending=True).head())

st.write("Podemos perceber que em 1927 já há uma inconsistência de valores. Vamos averiguar as categorias disponíveis deste ano para as duas tabelas.")
st.write("Para isso, há dois métodos diferentes em que podemos checar essas informações:")


with st.expander("1.) Eliminando aos poucos as inconsistências de categorias (em processo)"):
    st.table(df_limpo[df_limpo["Year"] == "1927/28"].value_counts("Category"))

    st.table(df2_limpo[df2_limpo["year_film"] == 1927].value_counts("category"))

    st.write("Podemos perceber que em uma das tabelas há a categoria `SPECIAL AWARD`, e ela é a responsável pela diferença. Portanto, vamos remover todas as instâncias dessa categoria para verificar se há algum valor restante.")

    # Removendo as categorias com SPECIAL AWARD de df2
    filtro2 = df2_limpo["category"] != "SPECIAL AWARD"
    df2_limpo = df2_limpo[filtro2]

    st.write(f"Total de linhas e colunas: {df2_limpo.shape}")
    st.dataframe(df2_limpo)

    st.write("Conferindo novamente quais os valores por ano de `df2`:")
    st.dataframe(df2_limpo.value_counts("year_film").reset_index().sort_values(by="year_film", ascending=True))
    st.dataframe(df_limpo.value_counts("Year").reset_index().sort_values(by="Year", ascending=True))




with st.expander("2.) Checando todas as categorias de uma só vez"):
    st.write("Neste método, iremos extrair todas as categorias e transformá-las em uma lista pela seguinte maneira.")
    st.write("Para `df`:")
    st.code("""
df_categorias = df.dropna(axis=0, subset=["Name", "Film"])
lista_df = df_categorias.value_counts("Category").reset_index()
lista_df = lista_df["Category"].sort_values(ascending=True).to_list()""")
    st.write("Resultado da lista (em forma de tabela):")
    df_categorias = df.dropna(axis=0, subset=["Name", "Film"])
    lista_df = df_categorias.value_counts("Category").reset_index()
    lista_df = lista_df["Category"].sort_values(ascending=True).to_list()
    st.dataframe(lista_df)
    # st.code(lista_df, wrap_lines=True)

    st.write("Para `df2`:")
    st.code("""
df2_categorias = df2.dropna(axis=0, subset=["name", "film"])
lista_df2 = df2_categorias.value_counts("category").reset_index()
lista_df2 = lista_df2["category"].sort_values(ascending=True).to_list()""")
    st.write("Resultado da lista (em forma de tabela):")
    df2_categorias = df2.dropna(axis=0, subset=["name", "film"])
    lista_df2 = df2_categorias.value_counts("category").reset_index()
    lista_df2 = lista_df2["category"].sort_values(ascending=True).to_list()
    st.dataframe(lista_df2)
    # st.code(lista_df2, wrap_lines=True)

    st.write("Agora iremos verificar quais categorias estão presentes em `df2` que não estão em `df` (já que o primeiro tem um número de linhas maior):")
    st.code("c = list(set(lista_df2) - set(lista_df))", language="python")

    c = list(set(lista_df2) - set(lista_df))
    c.sort()
    st.dataframe(c)

st.html("""<h2>Conclusão da análise prévia dos dados</h2>
Podemos, a partir disso, coletar algumas informações importantes e já tomar algumas decisões de acordo com algumas colunas:""")

st.write("Poderemos agora partir para a análise de dados feita de fato.")
st.write("")

# Parte 3 - Analisando os dados e levantando gráficos
st.subheader("3. Tratando os dados da planilha", divider="gray")
st.write("Texto aqui...")



st.html("""<br><br><br><br><br><br>
<details>r
<summary>How do I dropdown?</summary>
<br>
This is how you dropdown.
</details>
""")