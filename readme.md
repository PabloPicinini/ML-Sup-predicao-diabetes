# Predição de Diabetes usando Machine Learning

## Objetivo do Projeto

Este projeto tem como objetivo prever o **risco de diabetes** em indivíduos com base em dados de saúde e comportamentais, utilizando técnicas de **Machine Learning**. A previsão é realizada com base em variáveis históricas e fatores de risco, como Índice de Massa Corporal (IMC), colesterol, hipertensão e atividades físicas.

## Estrutura do Projeto

```bash
├── app
│   ├── images
│   │   ├── icone.png
│   │   ├── logo.png
│   ├── __init__.py
│   ├── main.py        # Aplicação Streamlit para realizar previsões com CSV
│   ├── prev_diabet.py # Função de previsão utilizando o modelo salvo
├── datasets
│   ├── diabetes_012_health_indicators_BRFSS2015.csv
│   ├── diabetes_binary_5050split_health_indicators_BRFSS2015.csv
│   ├── diabetes_binary_health_indicators_BRFSS2015.csv # CSV utilizado pelo modelo
├── venv               # Ambiente virtual Python
├── .gitignore         # Arquivos e pastas ignorados pelo Git
├── model_diabet.ipynb # Análise exploratória, feature engineering e criação do modelo final
├── readme.md
├── requirements.txt
├── scaler.pkl         # Scaler do StandardScaler para normalização dos dados de Input
├── svc_model_prev_diabet.pkl # Modelo SVC salvo
├── test_model.ipynb   # Teste de diferentes modelos e comparação de métricas
├── x_teste.csv        # Conjunto de teste para a aplicação
```

## Dataset Utilizado

- Dataset disponível no [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_health_indicators_BRFSS2015.csv)
    - **diabetes_binary_health_indicators_BRFSS2015.csv**: 
    
        Este dataset contém indicadores de saúde e comportamentais coletados pela pesquisa BRFSS (Behavioral Risk Factor Surveillance System) de 2015. Os dados incluem informações sobre atividades físicas, IMC, colesterol, pressão arterial, entre outros fatores.

## Objetivo

O objetivo deste projeto é prever o risco de **desenvolvimento de diabetes** com base em variáveis relacionadas ao estilo de vida e condições de saúde dos participantes.

## Modelos de Machine Learning Utilizados

Os seguintes algoritmos de Machine Learning foram testados durante o desenvolvimento do projeto:

- **Logistic Regression**
- **Decision Tree Classifier**
- **Support Vector Machine (SVM)**
- **K-Nearest Neighbors (KNN)**
- **XGBoost Classifier**
- **Random Forest Classifier**
- **Perceptron**
- **MLP Classifier**

Após a comparação entre os modelos, o **SVM (Support Vector Machine)** foi escolhido como o modelo final por apresentar a melhor performance em termos de acurácia.

## Detalhes do Modelo Final

- **Modelo Selecionado**: SVM (Support Vector Machine)
- **Hiperparâmetros**: `SVC(C=10, class_weight={0: 1, 1: 1.5}, probability=True, random_state=42)`
- **Acurácia do Modelo**: 86.57%
- O modelo foi salvo no arquivo `svc_model_prev_diabet.pkl`.

## Como Executar a Aplicação
1. Clone o repositório e instale as dependências:
   ```bash
   git clone https://github.com/PabloPicinini/ML-Sup-predicao-diabetes.git
   ```

2. **Instalar as dependências**:
- Ative o ambiente virtual e instale os pacotes necessários:
  ```bash
  cd predicao-diabetes
  .\venv\Scripts\activate  # Em Windows
  pip install -r requirements.txt
  ```

3. **Configurar o arquivo `kaggle.json`**:
   - Acesse sua conta no [Kaggle](https://www.kaggle.com/), vá até as configurações e baixe o arquivo de autenticação `kaggle.json`.
   - Coloque o arquivo `kaggle.json` na pasta `.kaggle` (se não tiver crie na pasta raiz) do seu projeto. 
   - O arquivo `kaggle.json` é necessário para fazer a autenticação ao baixar datasets diretamente do Kaggle via API.

4. Se desejar pode executar os arquivos dos modelos para verificar as Análises Exploratórias, Feature Engineering e os Modelos utilizados.

5. Execute o script da aplicação:
    ```bash
    streamlit run app/main.py
    ```

6. Acesse a aplicação no navegador 
- Forneça os dados de entrada e obtenha a previsão do risco de diabetes.
    - Dados de Inputs individuais;
    - Dados em formato CSV com o mesmo padrão utilizado no dattaset.

Isso iniciará a aplicação, onde você poderá fazer previsões e análises.
