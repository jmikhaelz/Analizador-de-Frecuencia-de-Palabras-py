#LIBRERIAS
import os                               #Manipulaciones comunes de nombre de ruta
import re                               #Operaciones con expresiones regulares
from unicodedata import normalize
import nltk                             #Procesamiento de lenguaje natural escrita
from nltk.tokenize import word_tokenize #Para procesar los espacios en palabras
from nltk.corpus import stopwords       #Palabras vacías o palabras comunes
from colorama import Fore, Style        #Manejos de colores de texto
import matplotlib.pyplot as plt         #Manejos de creacion de graficas
import numpy as np                      #Manejos matrices y arreglos multidimensionales
import pandas as pd                     #Manejo, análisis y procesamiento de datos
# Directorio que contiene los archivos de texto
directorio = input("\n Ingresa la dirección de la carpeta con los archivos de texto: ")

try: #Empezamos en revisar el contenido de los archivos de la carpeta
    for archivo in os.listdir(directorio):
        #separamos el nombre del archivo por el punto
        arch = archivo.split(sep='.')
        match arch[1]: #Revisamos que tipo de archivo se esta leyendo
            case "txt":
                # Conversion de color para el nombre del archivo
                colored_filename = Fore.BLUE + arch[0] + Style.RESET_ALL
                print("\n [TXT]" + "_"*30 + f" {colored_filename} " + "_"*30+"\n")
                #Hacemos lectura del documento
                ruta = os.path.join(directorio, archivo)
                with open(ruta, encoding="utf-8") as doc:
                    contenido = doc.read()
                    doc.close()
                    #Convertimos el texto en minusculas
                    contenido = contenido.lower()
                    #Limpiamos caracteres especiales por espacios, acentos
                    contenido = re.sub(r'[^\w\s]', '', contenido) #Quitamos caracteres especiales
                    contenido = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", contenido), 0, re.I) #Quitamos los acentos y limitamos que no modifique la ñ (NFD / descomposición canónica traduce cada carácter a su forma descompuesta)
                    #contenido = normalize( 'NFC', contenido) #(NFC / vuelve a componer caracteres precombinados)
                    #Separamos el texto por palabras
                    contenido = nltk.word_tokenize(contenido)
                    #Eliminaremos las stopwords y revisamos la longitud de la palabra si es mayor de 2
                    contenido = [word for word in contenido if word not in stopwords.words("english") and word not in stopwords.words("spanish") and len(word)>2]
                    #Frecuencia de las palabras
                    cnt = np.asarray(contenido)                     # Convertimos contenido de type:list a array
                    df = pd.DataFrame(cnt, columns=['Palabras'])    # Agregamos en una columna las palabras
                    df = df.groupby(['Palabras']).size().reset_index(name='Frecuencia') #Agrupamos las palabras dada a la frecuencia de veces que aparezcan
                    df.sort_values(by=['Frecuencia'],ascending=False, inplace=True) #Ordenamos las palabras dada a la frecuencia
                    df.reset_index(drop=True, inplace=True) #Reordenamos los indices por el ranking
                    print(df)   #Imprimimos la tabla
                    #Personalizamos la grafica
                    df.plot(marker='o',linestyle = ':',linewidth=0.5,c = '#138D75') #Cada palabra se reprentrara por un punto de color verde
                    #Fuentes para los letreros de los ejes y titulo
                    f1 = {'family': 'Arial', 'color': '#2471A3', 'size': 18}
                    f2 = {'family': 'Arial', 'color': '#7D3C98', 'size': 14}
                    f3 = {'family': 'Arial', 'color': '#F39C12', 'size': 14}
                    #Nombramos los letreros y ajustamos su fuente correspondiente
                    plt.title(archivo, fontdict=f1)
                    plt.xlabel("Indice (x)", fontdict=f2)
                    plt.ylabel("Frecuencia (y)", fontdict=f3)
                    #Almacenamos la grafica en la carpeta del programa
                    plt.savefig('graficas/'+arch[0], dpi=200)
                    df.to_csv('tablas/'+arch[0]+'.txt', index=False,sep="\t")
                    plt.show()
            case "pdf":
                # Conversion de color para el nombre del archivo
                colored_filename = Fore.GREEN + arch[0] + Style.RESET_ALL
                print("\n [PDF]" + "_"*30 + f" {colored_filename} " + "_"*30+"\n")
    
except Exception as e: #Si hay un error en un archivo de identificara
    print(f"\n <!> : {str(e)}")
