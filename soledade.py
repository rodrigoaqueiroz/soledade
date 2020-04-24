import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_excel("Soledade.xlsx")
#Removendo a coluna Matrícula (não é necessário para a análise)
df = df.drop(["Matrícula"], axis = 1)
worker = df.groupby("Servidor").sum().reset_index()
duplicates_removed = df.drop_duplicates("Servidor").sort_values(by = "Servidor")
df = duplicates_removed
gender = df["Gênero"].value_counts()
Male = gender[1]
Female = gender[0]


#Criando o gráfico de distribuição de M e F
labels = "F", "M"
size = gender.values
colors = ["#ff9999","#4287f5"]
explode = (0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(size, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.tight_layout()
plt.show()


duplicates_removed = df.drop_duplicates("Servidor").sort_values(by = "Servidor")
  
#Mostrar o salário de cada trabalhador (juntando os que tem dois empregos)
worker["Cargo"] = duplicates_removed["Cargo"].values
worker["Salário Bruto"].nlargest(5)


worker = worker.sort_values(by = "Salário Bruto", ascending = False, axis = 0)

def main():
    st.title("Folha salarial de Soledade-PB.")
    st.subheader("Janeiro de 2020")
    st.subheader('Analisando os dados')
    st.markdown('**Número de linhas:**')
    st.markdown(df.shape[0])
    st.markdown('**Visualizando o dataframe**')
    number = st.slider('Escolha o numero de linhas que deseja ver', min_value=1, max_value=50)
    st.dataframe(df.head(number))
    st.markdown('**Nome das colunas:**')
    st.markdown(list(df.columns))
    st.markdown('**Quantidade de funcionários do sexo masculino:**')
    st.markdown(Male)
    st.markdown('**Quantidade de funcionários do sexo feminino:**')
    st.markdown(Female)
    st.markdown('**Gráfico de distribuição**')
    st.image("distribuicao.png", width= 500)
    maiores = st.slider("Escolha a quantidade dos maiores salários que você deseja ver", min_value=1, max_value=100)
    st.dataframe(pd.DataFrame({"Funcionário": worker["Servidor"].head(maiores), 
                                   "Salário": worker["Salário Bruto"].nlargest(maiores), 
                                   "Cargo": worker["Cargo"].head(maiores) }))
    menores = st.slider("Escolha a quantidade dos menores salários que você deseja ver", min_value=1, max_value=100)
    st.dataframe(pd.DataFrame({"Funcionário": worker["Servidor"].tail(menores), 
                                   "Salário": worker["Salário Bruto"].tail(menores), 
                                   "Cargo": worker["Cargo"].tail(menores) }))
    select_method = st.radio('Escolha um metodo abaixo do salário:', ('Média', 'Moda'))
    st.markdown('Você selecionou : ' +str(select_method))
    if select_method == 'Média':
        mean = round(worker["Salário Bruto"].mean(), 2)
        st.markdown("A média do salário bruto é: " + str(mean))
    if select_method == 'Moda':
        moda = round(worker["Salário Bruto"].mode(), 2).values[0]
        st.markdown("A moda do salário bruto é: " + str(moda))
    st.markdown("**Distribuição de recebimento dos salários por unidade gestora:**")
    st.dataframe(df.groupby("Unidade Gestora").sum())

    st.markdown("**Feito com Pandas!**")
    st.image('https://media.giphy.com/media/KyBX9ektgXWve/giphy.gif', width=200)

if __name__ == "__main__":
    main()






    






