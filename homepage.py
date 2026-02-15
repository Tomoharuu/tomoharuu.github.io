import streamlit as st

st.header("Projeto de Análise de Dados", divider="gray")


st.write("""Este projeto tem como objetivo ser um demonstrativo de um projeto de análise de dados completo.

Isso inclui:

- **Passo a Passo** realizando desde a análise prévia de quais são os dados que estão sendo trabalhados, até a coleta, organização e por fim exibição dos dados de fato;
- **Análise Resumida:** uma página que conterá um "resumo" das principais informações obtidas no Passo a Passo, mostrando de uma forma mais direta as conclusões obtidas com o projeto;
- **Dashboards:** Apesar de este não ser um projeto focado na parte da exibição (os dados em si valem mais que a apresentação deles), também será elaborado um dashboard (possivelmente interativo) contendo um método de visualização interessante para a proposta do projeto.""")

st.write("Além disso")

st.write("Página ainda em construção!")
st.subheader("Sobre o Projeto")
with st.expander("Qual o tema do projeto?"):
    st.write("Aqui está uma descrição mais detalhada...")


with st.expander("Quais as tecnologias usadas?"):
    st.write("Aqui está uma descrição mais detalhada...")


with st.expander("Qual o objetivo do projeto?"):
    st.write("Aqui está uma descrição mais detalhada...")
