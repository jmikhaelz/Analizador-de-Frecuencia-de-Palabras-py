# Analizador de Frecuencia de Palabras

Este proyecto es un script en Python diseñado para analizar archivos de texto, procesar las palabras y generar gráficos de frecuencia. Es útil para obtener una visión general de las palabras más comunes en un conjunto de documentos.

## Requisitos

- Python 3.x
- Las siguientes bibliotecas de Python:
  - `os`
  - `re`
  - `unicodedata`
  - `nltk`
  - `colorama`
  - `matplotlib`
  - `numpy`
  - `pandas`

Puedes instalar las bibliotecas necesarias usando pip:

```bash
pip install nltk colorama matplotlib numpy pandas
```

## Uso

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener los archivos de texto que deseas analizar en una carpeta.
3. Ejecuta el script y proporciona la ruta de la carpeta cuando se te solicite.

```
python analizador_frecuencia.py
```

## Descripción del Script

El script realiza las siguientes acciones:

1. **Lectura de Archivos** : Lee todos los archivos de texto en la carpeta especificada.
2. **Procesamiento de Texto** :

* Convierte el texto a minúsculas.
* Elimina caracteres especiales y acentos.
* Tokeniza el texto en palabras.
* Elimina las palabras vacías (stopwords) en inglés y español.

1. **Análisis de Frecuencia** : Calcula la frecuencia de cada palabra y las ordena de mayor a menor.
2. **Generación de Gráficas** : Crea y guarda un gráfico de la frecuencia de palabras para cada archivo de texto.
3. **Salida de Datos** : Guarda los resultados en archivos CSV y muestra las gráficas.

## Ejemplo de Salida

El script genera una tabla de frecuencias y un gráfico para cada archivo de texto procesado. Aquí tienes un ejemplo de cómo se vería la salida:

```
 [TXT]______________________________ ejemplo.txt ______________________________

    Palabras  Frecuencia
0   ejemplo          10
1   palabra           8
2   texto             5
...

```

!Gráfico de Frecuencia

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
