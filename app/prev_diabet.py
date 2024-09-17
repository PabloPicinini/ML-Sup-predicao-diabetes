import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Cache para carregar o modelo e o scaler uma vez
@st.cache_resource
def load_model():
    return joblib.load('svc_model_prev_diabet.pkl')

@st.cache_resource
def load_scaler():
    return joblib.load('scaler.pkl')

if "historico" not in st.session_state:
    st.session_state.historico = []

def prev_diabet():
    # Carregar o modelo e o scaler
    model = load_model()
    scaler = load_scaler()

    # Título da aplicação
    st.title("Previsão de Diabetes")
    st.write("Insira os dados para obter uma predição.")

    # Seletor de funcionalidade na barra lateral
    option = st.sidebar.selectbox("Escolha uma opção", ["Formulário de Predição", "Predição por CSV"])

    if option == "Formulário de Predição":
        # Formulário com inputs baseados nas colunas
        with st.form(key="form_diabetes"):
            high_bp = st.selectbox("Você foi diagnosticado com pressão alta?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            high_chol = st.selectbox("Você já foi informado que tem colesterol alto?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            bmi = st.number_input('Índice de Massa Corporal (BMI)', min_value=10.0, max_value=60.0, value=25.0)
            smoke = st.selectbox("Você fumou pelo menos 100 cigarros na vida (5 maços)?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            stroke = st.selectbox("Você já teve um derrame?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            heart_disease = st.selectbox("Você já foi diagnosticado com doença cardíaca?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            phys_activity = st.selectbox("Você realizou atividade física nos últimos 30 dias?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            alcohol = st.selectbox("Consumo excessivo de álcool?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            gen_health = st.selectbox("Como você classificaria sua saúde geral?", [(1, 'Excelente'), (2, 'Muito Boa'), (3, 'Boa'), (4, 'Razoável'), (5, 'Ruim')], format_func=lambda x: x[1])
            mental_health_days = st.number_input("Dias de problemas de saúde mental", min_value=0, max_value=30, value=0)
            physical_health_days = st.number_input("Dias de problemas de saúde física", min_value=0, max_value=30, value=0)
            diff_walk = st.selectbox("Dificuldade para andar ou subir escadas?", [(1, 'Sim'), (0, 'Não')], format_func=lambda x: x[1])
            age_group = st.selectbox("Faixa etária", [(1, '18-24'), (2, '25-29'), (3, '30-34'), (4, '35-39'), (5, '40-44'), (6, '45-49'), (7, '50-54'), (8, '55-59'), (9, '60-64'), (10, '65-69'), (11, '70-74'), (12, '75-79'), (13, '80 ou mais')], format_func=lambda x: x[1])
            education = st.selectbox("Nível de escolaridade", [(1, 'Nunca frequentou a escola'), (2, 'Ensino Fundamental'), (3, 'Ensino Médio'), (4, 'Ensino Médio Completo'), (5, 'Ensino Superior'), (6, 'Pós-Graduação')], format_func=lambda x: x[1])
            income = st.selectbox("Faixa de renda anual", [(1, 'Menos de $10,000'), (2, '$10,000 a $14,999'), (3, '$15,000 a $19,999'), (4, '$20,000 a $24,999'), (5, '$25,000 a $34,999'), (6, '$35,000 a $49,999'), (7, '$50,000 a $74,999'), (8, '$75,000 ou mais')], format_func=lambda x: x[1])

            # Botão de submissão do formulário
            submit_button = st.form_submit_button(label="Fazer Predição")

            if submit_button:
                # Obter a data e hora atual formatada
                data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                # Coletando todos os inputs do formulário
                inputs = [
                high_bp[0], high_chol[0], bmi, smoke[0], stroke[0], heart_disease[0],
                phys_activity[0], alcohol[0],
                gen_health[0], mental_health_days, physical_health_days, 
                diff_walk[0], age_group[0], education[0], income[0]
            ]

                # Convertendo inputs para um array 2D
                inputs_2d = [inputs]

                # Transformar os dados
                inputs_scaled = scaler.transform(inputs_2d)

                # Fazendo a predição
                resultado = model.predict(inputs_scaled)[0]

                # Mostrando o resultado
                if resultado == 1:
                    st.write("Alto risco de diabetes. Recomendamos que consulte um médico.")
                else:
                    st.write("Continue mantendo hábitos saudáveis.")

                # Criando um dicionário com os dados da predição
                predicao = {
                "Data/hora": data_hora_atual,
                "Resultado": "Alto risco" if resultado == 1 else "Baixo risco",
                "Pressão Alta": high_bp[1],
                "Colesterol Alto": high_chol[1],
                "BMI": bmi,
                "Fumou 100 Cigarros": smoke[1],
                "Derrame": stroke[1],
                "Doença Cardíaca": heart_disease[1],
                "Atividade Física": phys_activity[1],
                "Consumo de Álcool": alcohol[1],
                "Saúde Geral": gen_health[1],
                "Dias de Problemas de Saúde Mental": mental_health_days,
                "Dias de Problemas de Saúde Física": physical_health_days,
                "Dificuldade para Andar": diff_walk[1],
                "Faixa Etária": age_group[1],
                "Educação": education[1],
                "Renda Anual": income[1]
            }

                # Adicionando o registro ao histórico
                st.session_state.historico.append(predicao)

                # Convertendo o histórico para um DataFrame
                df_historico = pd.DataFrame(st.session_state.historico)

                # Função para aplicar estilo condicional
                def highlight_risk(row):
                    return ['background-color: lightcoral' if row['Resultado'] == 'Alto risco' else '' for _ in row]

                # Mostrando o DataFrame de Histórico
                st.write("### Histórico de Predições:")
                st.dataframe(df_historico.style.apply(highlight_risk, axis=1))

        # Botão para limpar o histórico
        if st.button("Limpar Histórico"):
            st.session_state.historico = []

    elif option == "Predição por CSV":
        st.write("### Carregar e Processar CSV")

        # Botão de upload de arquivo CSV
        uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

        if uploaded_file is not None:
            # Exibir mensagem de carregamento
            with st.spinner("Processando o arquivo CSV..."):
                # Ler o arquivo CSV
                data = pd.read_csv(uploaded_file)

                # Verificar se os dados têm o mesmo número de colunas que o scaler espera
                expected_columns = scaler.feature_names_in_  # Obtém os nomes das colunas do scaler
                if len(data.columns) != len(expected_columns):
                    st.error("Número de colunas no CSV não corresponde ao esperado.")
                else:
                    # Transformar os dados
                    data_scaled = scaler.transform(data)

                    # Fazer predições
                    predictions = model.predict(data_scaled)

                    # Adicionar as predições ao DataFrame
                    data['Prediction'] = predictions

                    # Gerar o arquivo CSV com as predições
                    csv = data.to_csv(index=False)
                    st.download_button(
                        label="Baixar CSV com Predições",
                        data=csv,
                        file_name='predicoes.csv',
                        mime='text/csv'
                    )

                    # Mostrar o DataFrame com predições
                    st.write("### Dados com Predições:")
                    st.dataframe(data)

if __name__ == "__main__":
    prev_diabet()
