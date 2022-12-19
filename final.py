#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from PIL import Image
st.markdown("<h1 style='text-align: center; color: white;'>Universidad Nacional de San Agustín de Arequipa</h1>", unsafe_allow_html=True)

st.subheader('Escuela Profesional de Ingeniería de Telecomunicaciones')
st.markdown('##') 

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://www.unsa.edu.pe/jaku/wp-content/themes/observatorio/img/unsa-logo.png)*")

st.markdown("<h2 style='text-align: center; color: white;'>Ingeniero Renzo Bolivar - Docente DAIE </h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Computación 1</h2>", unsafe_allow_html=True)

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.markdown("<h1 style='text-align: center; color: white;'>Grupo B - N°1</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Alumnos</h1>", unsafe_allow_html=True)
    
st.subheader('                                  -Gonzales Jara, Edwar Gareth')
st.subheader('                                  -Noa Mamani, Max Geovanny (Coordinador del grupo)')
st.subheader('                                  -Vera Apaza, Patrick Anderson')
st.subheader('                                  -Vilca Conde, David Geordy')
st.subheader('                                  -Mendoza Contreras, Abel Noe')
st.subheader('                                  -Peña Quispe, Jeampiere Gary')


st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.subheader('INVESTIGACIÓN FORMATIVA')
st.subheader('PROYECTO FINA')
st.subheader('PYTHON - Inteligencia Artificial')


st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.write("OBJETIVOS")

st.write("*Los Objetivos de la investigación formativa son:*")
st.write("*Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook*")
st.write("*Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).*")
st.write("*Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.*")


st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.subheader('Aplicación en IA')
st.subheader('Sistema Recomendador')

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.write("*El Sistema recomendador deberá encontrar la <strong>compatibilidad o similitud</strong> entre un grupo de personas encuestadas, en las áreas de:*")
st.write("*Musica*")
st.write("*Peliculas*")  
st.write("*Comida*")
st.write("*Lugares que desean Conocer*")   
st.write("*Obras de Arte*") 

st.write("*La compatibilidad o similitud será encontrada con el algoritmo de Correlación de Pearson y será verificada con la La Matrix de Correlación de Pearson con una librería de Python y utilizando una función personal*")  

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.subheader('Base Teórica')
st.subheader('Análisis de Correlación')

st.write("*El **análisis de correlación** es el primer paso para construir modelos explicativos y predictivos más complejos.*")

st.write("*A menudo nos interesa observar y medir la <strong>relación entre 2 variables numéricas</strong> mediante el análisis de correlación.*")
st.write("*Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo.*")
st.write("*Para poder tener el  Datset hay que recolectar información a travez de encuentas.*")


st.write("*¿Qué es la correlación?*")

st.write("*La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la **tendencia (creciente o decreciente) en los datos**.*")
st.write("*Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.*")

st.write("*Dos variables ***se correlacionan cuando muestran una tendencia creciente o decreciente***.*")

st.write("*¿Cómo se mide la correlación?*")

st.write("*Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*.*")

st.subheader('Correlación de Pearson ')


st.write("*El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.*")


st.write("*Es el método de correlación más utilizado, pero asume que:*")
# 
st.write("*- La tendencia debe ser de tipo lineal.*")
st.write("* - No existen valores atípicos (outliers).*")
st.write("* - Las variables deben ser numéricas.*")
st.write("*- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).*")
# 
st.write(*" Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.*")

st.subheader('Cómo se interpreta la correlación ')

st.write("* El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.*")
st.write("*- un valor positivo indica una relación directa o positiva,*")
st.write("* - un valor negativo indica relación indirecta, inversa o negativa,*")
st.write("*n valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).*")

st.write("*magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.*")
st.write("*- si la correlación vale $1$ o $-1$ diremos que la correlación es “perfecta”,*")
st.write("*- si la correlación vale $0$ diremos que las variables no están correlacionadas.*")

        


st.subheader('Fórmula Coeficiente de Correlación de Pearson ')

st.write("* $$ r(x,y)=\frac{\sum_{i=1}^{n}(x_{i}-\overline{x})(y_{i}-\overline{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\overline{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\overline{y})^{2}}}$$*")

st.write("***Distancia Euclidiana**: La distancia euclidiana es la generalización del __`teorema de Pitágoras`__.*")

st.write("* $$d_{E}(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}$$*")

st.write("* **Regresión Lineal**: La regresión lineal se usa para encontrar una __`relación lineal entre el objetivo y uno o más predictores`__.*")

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png)*")

st.write("* Coeficiente de correlación de Pearson*")
st.write("* En estadística, el coeficiente de correlación de Pearson es una medida de dependencia lineal entre dos variables aleatorias cuantitativas. A diferencia de la covarianza, la correlación de Pearson es independiente de la escala de medida de las variables.*")
 
st.write("*De manera menos formal, podemos definir el coeficiente de correlación de Pearson como un índice que puede utilizarse para medir el grado de relación de dos variables siempre y cuando ambas sean cuantitativas y continuas.*")

st.write("*Interpretación del coeficiente de correlación de Karl Pearson*")
st.write("* El coeficiente de correlación de Pearson tiene el objetivo de indicar cuán asociadas se encuentran dos variables entre sí por lo que:*")
 
st.write("*Correlación menor a cero: Si la correlación es menor a cero, significa que es negativa, es decir, que las variables se relacionan inversamente*")
st.write("*Cuando el valor de alguna variable es alto, el valor de la otra variable es bajo. Mientras más próximo se encuentre a -1, más clara será la covariación extrema. Si el coeficiente es igual a -1, nos referimos a una correlación negativa perfecta.*")
 
st.write("*Correlación mayor a cero: Si la correlación es igual a +1 significa que es positiva perfecta. En este caso significa que la correlación es positiva, es decir, que las variables se correlacionan directamente.*")
 
st.write("*Cuando el valor de una variable es alto, el valor de la otra también lo es, sucede lo mismo cuando son bajos. Si es cercano a +1, el coeficiente será la covariación.*")
 
st.write("*Correlación igual a cero: Cuando la correlación es igual a cero significa que no es posible determinar algún sentido de covariación. Sin embargo, no significa que no exista una relación no lineal entre las variables.*")
 
st.write("*Cuando las variables son independientes significa que estas se encuentra correlacionadas, pero esto nos significa que el resultado sea verdadero.*")
 

st.write("*Ventajas y desventajas del coeficiente de correlación de Pearson*")
st.write("*Entre las principales ventajas del coeficiente de correlación de Karl Pearson se encuentran:*")

st.write("*El valor es independiente de cualquier unidad que se utiliza para medir las variables.*")
st.write("*Si la muestra es grande, es más probable la exactitud de la estimación.*")
st.write("*Alguna de las desventajas del coeficiente de correlación son:*")
 
st.write("*Es necesario las dos variables sean medidas a un nivel cuantitativo continuo.*")
st.write("* La distribución de las variables deben ser semejantes a la curva normal.*")

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")

st.subheader('Propuesta')

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")


st.subheader('Dataset')




st.write("*Para poder tener el  <strong>Datset</strong> hay que recolectar información con una encuenta elaborada por nosotros.*")


st.subheader('Encuesta ejemplo:')

st.write("* La encuesta la realizamos en Google-Form donde se solicitara escoger un Dibujo Animado*")
st.write("*Donde si escoge 1 es el que menos le gusta hasta 5 que es el que mas le gusta (escala de liker)*")

st.subheader('Formulario de Google (Preguntas) ')
st.subheader('30 lugares increíbles para visitar en Perú')

st.write("* Machu Picchu")
st.write("* Cusco")
st.write("* La fortaleza de Sacsayhuamán")
st.write("*Maras y Moray")
st.write("*Ollantaytambo*")
st.write("*Písac*")
st.write("*Choquequirao*")
st.write("*Monasterio de San Francisco*")
st.write("*Museo Larco*")
st.write("*Pachacámac*")
st.write("*Líneas de Nazca*")
st.write("*Hacer el tour de tubulares en la Huacachina*")
st.write("*La Reserva nacional de Paracas*")
st.write("*Convento de Santa Catalina*")
st.write("*Cañón del Colca*")
st.write("*Lago Titicaca*")
st.write("*Fortaleza de Kuélap*")
st.write("*Catarata de Gocta*")
st.write("*Mausoleos de Revash*")
st.write("*Parque nacional de Huascarán*")
st.write("* Chavín de Huantar*")
st.write("*Caral*")
st.write("* Trujillo*")
st.write("*Chan Chan*")
st.write("* Huaca de la Luna*")
st.write("*Museo Tumbas Reales de Sipán*")
st.write("*Los Manglares de Tumbes*")
st.write("*Ayacucho*")
st.write("*La Reserva de Pacaya Samiria*")
st.write("*El Parque nacional del Manu*")


st.subheader('Formulario de Google (Imagenes) ')

# ![Captura%20de%20pantalla%20de%202022-12-08%2012-24-11.png](attachment:Captura%20de%20pantalla%20de%202022-12-08%2012-24-11.png)

# ![Captura%20de%20pantalla%20de%202022-12-08%2012-19-02.png](attachment:Captura%20de%20pantalla%20de%202022-12-08%2012-19-02.png)
# 

# #### Formulario de Google (Preprocesamiento)
# ![Captura%20de%20pantalla%20de%202022-12-08%2012-26-17.png](attachment:Captura%20de%20pantalla%20de%202022-12-08%2012-26-17.png)

# In[ ]:


#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd


# In[ ]:


#archivo CSV separado por comas
encuestaLTP = pd.read_csv('LTP.csv')
#leer  lineas
encuestaLTP


# In[ ]:


encuestaLTP.shape


# In[ ]:


encuestaLTP.dtypes


# In[ ]:


encuestaLTP.isnull().sum()


# ## Imputación de NaNs por la media

# In[ ]:


for dat in encuestaLTP.columns[1:]:
    encuestaLTP[dat].fillna(encuestaLTP[dat].mean(),inplace=True)
encuestaLTP


# In[ ]:


encuestaLTP.isnull().sum()


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 2.- Correlación de Pearson  (Similitud)

# In[ ]:


n = encuestaLTP[encuestaLTP.columns[1:]].to_numpy()
m = encuestaLTP[encuestaLTP.columns[0]].to_numpy()
print(n)
print(m)
n[8]


# ## 3.- Correlación en Pandas

# In[ ]:


n.T


# In[ ]:


df = pd.DataFrame(n.T, columns = m)
df


# In[ ]:


m_corrpanda = df.corr()
m_corrpanda


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 4.- Matrix de Correlación

# In[ ]:


m_corrpanda


# In[ ]:


m_corrpanda = np.round(m_corrpanda, 
                       decimals = 4)  
  
m_corrpanda


# ## Mayor Numero

# In[ ]:


m_corrpanda[m_corrpanda>=1] = -0.4
m_corrpanda


# In[ ]:


m_corrpanda.max().sort_values(ascending=False)


# In[ ]:


x = m_corrpanda[m_corrpanda.columns[0:]].to_numpy()
print(x)


# In[ ]:


# Inicializar y asumir que el mayor está en el primer elemento; solo para inicializar
mayor =x[0][0]
# Momento de recorrer la matriz y obtener el mayor
for fila in x:
    for valor in fila:
        if valor > mayor:
            mayor = valor
print("De la matriz: ")
print(x)
print(f"el mayor es {mayor}")
x[x>=mayor] = 0
mayor =x[0][0]
for fila in x:
    for valor in fila:
        if valor > mayor:
            mayor = valor
print(f"el 2domayor es {mayor}")


# ## Gráfica de Calor

# In[ ]:




# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.heatmap(data=m_corrpanda) #CORRELACION DE PANDAS DEL PROFESOR
plt.show


# <div class="alert alert-info">
# 
#     
#    **HALLAR**: a partir de la matriz de correlación en  <strong>Pandas</strong> .
#     
#    **Instalar** : `matplotlib` `seaborn`
#     
# </div>

# ## 5.- RESULTADOS 

# Los resultados de similitud obtenidos en **Dibujos Animados** según la tabla de **Correlación** con los siguientes encuestados:
# 
#  1. _dmejiagu@unsa.edu.pe_ y _diquiapazam@unsa.edu.pe_  obtienen el **PRIMER** indice mas alto de similitud 
#  
#  2. _dmejiagu@unsa.edu.pe_ y _fargotem@unsa.edu.pe_ obtienen el **SEGUNDO** indice mas alto de similitud 

# <div class="alert alert-info">
# 
#     
#    **HALLAR**: a partir de la matriz de correlación en  <strong>Pandas</strong>. A simple vista se puede observar los resultados, pero para una matriz mas grande se debe programar una `función` o `método` para que **localice los dos usuarios con mas alto valos de correlación**.
#     
# </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Validación de Resultados</h1> </center> 

# In[ ]:





# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## Validación - Matrix de Correlación

# 
# <div class="alert alert-info">
# 
#    Se debe llenar la tabla de __VALIDACIÓN de la Matriz de Correlación__ con los valores de `Similitud` obtenidos
#     
#     
#    En `NUMPY` a partir de las matrices `n` y `m` con funciones.
#     
# </div>

# # Función para determinar el factor de correlacion de Pandas Mio

# Se realiza la validación de los resultados obtenidos con la   `Matriz de Correlación de Pearson` en `Numpy` 
#  

# In[ ]:


n = encuestaLTP[encuestaLTP.columns[1:]].to_numpy()
m = encuestaLTP[encuestaLTP.columns[0]].to_numpy()
print(n)
print(m)


# In[ ]:


n[4,0]


# In[ ]:


n[5]


# In[ ]:


m[-1]


# In[ ]:


#Validación de resultados
#Empezamos con los calculos de los valores de la matriz de correlacion, apoyandonos de las librerias cargadas anteriormente
import math


# In[ ]:


#sizes = np.random.uniform(15, 80, len(n[0]))
#colors = np.random.uniform(15, 80, len(n[0]))


#fig, ax = plt.subplots()

#ax.scatter(n[0], n[2], s=sizes, c=colors, vmin=0, vmax=100)

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))

plt.scatter(n[0], n[2], c='red', s=17)
plt.show()


# In[ ]:



# Distancia euclidiana
import math
def distancia(x,y):
    suma = 0
    c = 0
    for n in x:
        print(c)
        suma = suma + pow((x[c]-y[c]),2)
        c += 1
    return math.sqrt(suma)

print('\n\n\t\tDistancia Euclidiana = ', distancia(n[0],n[2]))  


# In[ ]:



def corrpson(a,b):
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    cont5=0
    cont6=0
    for n in a:
        cont1=cont1+((a[cont4]-(a.mean()))*((b[cont4]-(b.mean()))))
        cont4 += 1
        num=cont1
    for m in a:
        cont2=cont2+pow((a[cont5]-(a.mean())),2)
        cont3=cont3+pow((b[cont6]-(b.mean())),2)
        cont5+= 1
        cont6+= 1
    return (num/((math.sqrt(cont2))*(math.sqrt(cont3))))

m_corr_mio=[]
for columna in range(len(m)):
    m_corr_mio.append([0]*len(m) )
for columna in range(len(m)):
    for fila in range(len(m)):
        m_corr_mio[columna][fila]=(corrpson(n[columna],n[fila]))
    print('')
print('El coeficiente de Pearson es:')
print(m_corr_mio)


# In[ ]:


##Ordenando la correlación mía con ayuda de pandas

corr_mio_ordenada=pd.DataFrame(data=m_corr_mio,columns=m)

corr_mio_ordenada


# In[ ]:


corr_mio_ordenada[corr_mio_ordenada>=0.99] = -0.4
corr_mio_ordenada


# In[ ]:


corr_mio_ordenada.max().sort_values(ascending=False)


# In[ ]:


corr_mio_ordenada=pd.DataFrame(data=m_corr_mio,columns=m)


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# In[ ]:


print(m[0])
m_corr_mio[0]


# In[ ]:


## Grafica de calor mío
sns.heatmap(m_corr_mio)
plt.show


# In[ ]:


sns.heatmap(data=m_corrpanda) #grafica DE PANDAS DEL PROFESOR
plt.show


# <center> <h1>Conclusiones</h1> </center> 

#  <div class="alert alert-info">
#     
#    - ¿Se valido o no los resultados?
#     Es validado los resultados con la correlacion de m_corrpanda y la validacion de pandas "m_corr_mio"
#    
#     - Los resultados Validados son:
#     Los 2 primer mayor resultados
#     
#     m_corr pandas:
# 
#  el mayor es:  
# dpilaresc@unsa.edu.pe      0.8050
# el 2domayor es:
# rramosmont@unsa.edu.pe     0.8050
# 
#     m_corrpanda_mio:
#     
#     el 1ermayor es:
# dpilaresc@unsa.edu.pe    0.8049837428908978
#     
#     el 2domayor es:
# rramosmont@unsa.edu.pe   0.7902805620025483
#     
# - ¿Es efectivo el metodo de correlación de pearson?
# Si porque valor es independiente de cualquier unidad que se utiliza para medir las variables.
# Si la muestra es grande, es más probable la exactitud de la estimación.
# Alguna de las desventajas del coeficiente de correlación son:
# 
# Es necesario las dos variables sean medidas a un nivel cuantitativo continuo.
# La distribución de las variables deben ser semejantes a la curva normal.
#     
# - Correlación de Pearson y Regresión Lineal, ¿cual es su relación?
# El coeficiente de correlación lineal es una medida de regresión que sirve para establecer una relación lineal entre dos variables. De esta manera, su cálculo permite conocer con exactitud el grado de dispersión de los valores  de una variable en relación con una media para dicha variable.
#        
#     
#  </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# ## Referencia

# - __Profesor de Matematicas__: `John Gabriel Muñoz Cruz`
# https://www.linkedin.com/in/jgmc
# Mayor y menor de matriz en Python
# https://parzibyte.me/blog/2020/11/27/mayor-menor-matriz-python/
# Correlación Lineal en Python
# https://www.youtube.com/watch?v=UUQMstPRfFM&ab_channel=RocioChavezCienciadeDatos
# Coeficiente de correlación de Pearson - Aplicando la formula
# https://www.youtube.com/watch?v=FS2xpTq5t38&ab_channel=MarymiliSegura
# Cómo usar NUMPY y qué son nd-ARRAYS 🐍💻 [Curso Python Data Science Español]
# https://www.youtube.com/watch?v=fczpaVSwGCA&ab_channel=RafaGonzalezGouveia
# Pandas - Ejercicio 115: Reemplazar los Valores NaN con un Valor Específico con la Función fillna
# https://www.youtube.com/watch?v=PAU92GUyEt4&ab_channel=JohnOrtizOrdo%C3%B1ez
# Correlación de Pearson y cómo crear Mapas de Calor de la Matriz de Correlaciones con Python
# https://www.youtube.com/watch?v=IBMrXyTR6CU&ab_channel=C%C3%B3digoM%C3%A1quina
# Correlación lineal con Python
# https://www.cienciadedatos.net/documentos/pystats05-correlacion-lineal-python.html
# El coeficiente de correlación de Pearson (con ejemplo en Python)
# https://medium.com/@hdezfloresmiguelangel/el-coeficiente-de-correlaci%C3%B3n-de-pearson-con-ejemplo-en-python-6e8588f67e35
# Cómo crear una matriz de correlación en Python
# https://statologos.com/matriz-de-correlaciones-python/
# Data Science: Coeficiente de Correlación de Pearson
# https://electroboveda.blogspot.com/2019/08/data-science-coeficiente-de-correlacion.html
# a
# 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)
