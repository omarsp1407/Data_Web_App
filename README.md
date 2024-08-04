# Generador de Gráficos con Streamlit

Esta aplicación web utiliza Streamlit para generar gráficos interactivos utilizando Plotly Express. Actualmente, la aplicación permite generar un histograma y un gráfico de dispersión a partir de los datos de un conjunto de datos de vehículos usados.

## Descripción

La aplicación carga un conjunto de datos de vehículos usados y permite al usuario generar gráficos interactivos con solo presionar un botón. Los gráficos disponibles son:

- Histograma del odómetro de los vehículos.
- Gráfico de dispersión que muestra la relación entre el odómetro y el precio de los vehículos.

## Requisitos

- Python 3.7+
- Streamlit
- Pandas
- Plotly

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En macOS/Linux
    .\env\Scripts\activate   # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

1. Asegúrate de que el archivo `vehicles_us.csv` esté en el directorio `dataset` dentro del proyecto.

2. Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```

3. Abre tu navegador y navega a `http://localhost:8501` para ver la aplicación.

## Funcionamiento

La aplicación se compone de los siguientes elementos:

1. **Lectura de Datos:** Los datos se leen del archivo CSV `vehicles_us.csv` ubicado en el directorio `dataset`. 
   ```python
   car_data = pd.read_csv('dataset/vehicles_us.csv')