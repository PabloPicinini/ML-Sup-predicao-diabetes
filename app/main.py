import streamlit as st
from PIL import Image
import os
import joblib
from prev_diabet import prev_diabet


# Obtém o caminho do diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para a imagem
image_icone = os.path.join(current_directory, "images", "icone.png")
image_page = os.path.join(current_directory, "images", "logo.png")
# Abre a imagem
img = Image.open(image_icone)



# Configura a página do Streamlit
st.set_page_config(page_title="Predição Diabetes", page_icon=img, layout="wide")

# Verifica se a configuração da página já foi feita
if 'page_config_done' not in st.session_state:
    # Marca a configuração como feita
    st.session_state.page_config_done = True

# Função para o menu lateral e navegação
def sidebar_menu():
    sidebar_img = Image.open(image_page)
    st.sidebar.image(sidebar_img, use_column_width=True)

    # Menu principal do sidebar
    st.sidebar.markdown("## Selecione a Página")
    page = st.sidebar.selectbox(
        "Selecione",
        [   "Home Page",
            "Predição de Diabetes"], 
        format_func=lambda page: page
    )
    return page

# Função para a página inicial (home)
def home_page(): 
    tit1, tit2 = st.columns((0.1, 1))
    tit2.title("Predição de Diabetes")
    
     # Descrição do Projeto
    st.write("""
    ### Utilizando Machine Learning para Predição de Diabetes

    ---

    #### Sobre o Projeto
    Este modelo foi desenvolvido com o objetivo de prever o **risco de diabetes** em pacientes, utilizando dados de saúde e comportamentais. 
    A aplicação usa técnicas de aprendizado supervisionado para analisar variáveis relacionadas a fatores de risco conhecidos para o diabetes, como:
    - Índice de Massa Corporal (IMC)
    - Histórico de pressão e colesterol altos
    - Atividade física e dieta
    - Fatores de risco cardíacos

    **Problema a ser resolvido:**

    O diagnóstico precoce de diabetes é crucial para prevenir complicações de saúde a longo prazo. Governos, instituições de saúde e indivíduos precisam de ferramentas que ajudem a identificar possíveis casos de diabetes antes que os sintomas se tornem graves. 

    Este modelo auxilia na:
    - **Identificação precoce** de indivíduos em risco.

    A previsão é feita com base em variáveis históricas e fatores de risco, contribuindo para uma abordagem preventiva da saúde.

    ---

    ### Objetivo:
    Prever o risco de **desenvolvimento de diabetes** em indivíduos com base em variáveis relacionadas ao estilo de vida e condições de saúde.

    ---

    ### Modelo de Machine Learning Utilizado: 
    - SVM
        - Parâmetros: (C=10, class_weight={0: 1, 1: 1.5}, probability=True, random_state=42)

                          
    ### Métricas de Avaliação

    | Métrica                            | Valor                                      |
    |------------------------------------|--------------------------------------------|
    | **Acurácia**                       | 0.8657                                     |
    | **Precisão (Classe 0)**            | 0.82                                       |
    | **Precisão (Classe 1)**            | 0.93                                       |
    | **Recall (Classe 0)**              | 0.94                                       |
    | **Recall (Classe 1)**              | 0.79                                       |
    | **F1 Score (Classe 0)**            | 0.87                                       |
    | **F1 Score (Classe 1)**            | 0.86                                       |
    | **Curva ROC**                      | 0.92                                       |

    ### Pontuações de Validação Cruzada

    | Validação Cruzada                  |
    |------------------------------------|
    | 0.8628                             |
    | 0.8665                             |
    | 0.8704                             |
    | 0.8630                             |
    | 0.8659                             |
    | **Média das Pontuações**            | 0.8657                                     |

    ### Matriz de Confusão para Modelo SVC

    |               | **Classe 0** | **Classe 1** |
    |---------------|--------------|--------------|
    | **Classe 0**  | 9822         | 646          |
    | **Classe 1**  | 2182         | 8409         |

    ### Relatório de Classificação

    | Classe       | Precisão | Recall | F1-Score | Suporte |
    |--------------|----------|--------|----------|---------|
    | 0            | 0.82     | 0.94   | 0.87     | 10468   |
    | 1            | 0.93     | 0.79   | 0.86     | 10591   |
    | **Média**    | 0.87     | 0.87   | 0.87     | 21059   |
    | **Acurácia** |          |        | 0.87     | 21059   |
    | **Macro Avg**| 0.87     | 0.87   | 0.87     | 21059   |
    | **Weighted Avg** | 0.87  | 0.87   | 0.87     | 21059   |

    ### Melhor Modelo

    - **Modelo**: SVC(C=10, class_weight={0: 1, 1: 1.5}, probability=True, random_state=42)
    - **Acurácia**: 0.8657


    ---

    ## Funcionalidades:

    Aqui estão as principais funcionalidades disponíveis no aplicativo:

    1. **Previsão do Risco de Diabetes**: Insira dados como IMC, histórico de saúde, entre outros para obter uma previsão sobre o risco de diabetes.
    2. **Análise de Fatores de Risco**: Explore como cada fator (pressão alta, colesterol, atividade física) influencia o risco de diabetes.
    3. **Simulador de Saúde**: Simule e compare diferentes cenários de hábitos e condições de saúde e veja como eles impactam o risco de desenvolver diabetes.
    4. **Predição por CSV**: Carregue um CSV para realizar a predição desejada.
    ---

    ### Como usar:

    1. Preencha os campos do formulário com suas informações de saúde e estilo de vida.
    2. Insira variáveis como **IMC**, **colesterol**, **pressão alta** e outras condições.
    3. Clique no botão para realizar a previsão e visualizar o resultado.
    4. Explore diferentes cenários para analisar o impacto de mudanças de comportamento no risco de diabetes.

    """)

# Função principal para renderizar o conteúdo baseado na página selecionada
def main():
    page = sidebar_menu()

    if page == "Home Page":
        home_page()
    elif page == "Predição de Diabetes":
        prev_diabet()

    


# Executa a aplicação
if __name__ == "__main__":
    main()
