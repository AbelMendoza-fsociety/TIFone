#!/usr/bin/env python
# coding: utf-8

# <center> <h1>Universidad Nacional de San Agustín de Arequipa</h1> </center> 
# <center> <h1>Escuela Profesional de Ingeniería de Telecomunicaciones</h1> </center> 
# 
# <center> <h1> </h1> </center> 
# 
# <center><img src="https://www.unsa.edu.pe/wp-content/uploads/sites/3/2018/05/Logo-UNSA.png" width="380" height="4200"></center>
# 

# <center> <h2>Ingeniero Renzo Bolivar - Docente DAIE</h2> </center> 

# <center> <h1>Curso : Computación 1</h1> </center> 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h2>GRUPO A - Nº70</h2> </center> 
# <h2>Alumnos:  </h2>
# <h2>    
# 
#     Juanito los Palotes
#     Pedrito Infante
#     Jorge Negrete
# </h2>
# 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h1>INVESTIGACIÓN FORMATIVA</h1> </center> 
# <center> <h1>PROYECTO FINAL</h1> </center> 
# <center> <h1>PYTHON - Inteligencia Artificial</h1> </center> 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# ## OBJETIVOS

# Los Objetivos de la investigación formativa son:
# 
# - **Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.
# - **Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).
# - **Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h1>Aplicación en IA</h1> </center> 
# <center> <h1>Sistema Recomendador</h1> </center> 

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <div class="alert alert-info">
# El Sistema recomendador deberá encontrar la <strong>compatibilidad o similitud</strong> entre un grupo de personas encuestadas, en las áreas de:
# 
# </div>

# <div class="alert alert-info">
#     
#    -Musica
#    
#    -Peliculas
#     
#    -Comida
#     
#    -Lugares que desean Conocer
#     
#    -Obras de Arte
# 
#     
# 
# 
#     
# </div>

# <div class="alert alert-info">
# 
#     
#    La <strong>compatibilidad o similitud</strong> será encontrada con el algoritmo de <strong>Correlación de Pearson</strong> y será verificada con la <strong>La Matrix de Correlación de Pearson con una librería de Python y utilizando una función personal</strong>
#     
# </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Base Teórica</h1> </center> 

# ## Análisis de Correlación

# El **análisis de correlación** es el primer paso para construir modelos explicativos y predictivos más complejos.

# <div class="alert alert-info">
# 
#    A menudo nos interesa observar y medir la <strong>relación entre 2 variables numéricas</strong> mediante el análisis de correlación. 
#    Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier <strong>modelo explicativo o predictivo más complejo</strong>.
#    Para poder tener el  Datset hay que recolectar información a travez de encuentas.
#     
# </div>

# ### ¿Qué es la correlación?

# La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la **tendencia (creciente o decreciente) en los datos**.
# 
# Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.
# 
# Dos variables ***se correlacionan cuando muestran una tendencia creciente o decreciente***.

# ### ¿Cómo se mide la correlación?

# Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*. 

# ### Correlación de Pearson

# <div class="alert alert-info">
# El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.
# </div>

# Es el método de correlación más utilizado, pero asume que:
# 
#  - La tendencia debe ser de tipo lineal.
#  - No existen valores atípicos (outliers).
#  - Las variables deben ser numéricas.
#  - Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).
# 
# Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.

# ### Cómo se interpreta la correlación

# El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
#  - un valor positivo indica una relación directa o positiva,
#  - un valor negativo indica relación indirecta, inversa o negativa,
#  - un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).

# La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
#  - si la correlación vale $1$ o $-1$ diremos que la correlación es “perfecta”,
#  - si la correlación vale $0$ diremos que las variables no están correlacionadas.

# 
# <center><img src="https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png" width="700" height="4200"></center>
# 
# 
# 

# <center> <h3>Fórmula Coeficiente de Correlación de Pearson</h3> </center>  
# <center> <h3> </h3> </center> 
# $$ r(x,y)=\frac{\sum_{i=1}^{n}(x_{i}-\overline{x})(y_{i}-\overline{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\overline{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\overline{y})^{2}}}$$

# **Distancia Euclidiana**: La distancia euclidiana es la generalización del __`teorema de Pitágoras`__.

# $$d_{E}(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}$$

# **Regresión Lineal**: La regresión lineal se usa para encontrar una __`relación lineal entre el objetivo y uno o más predictores`__.

# ![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png)

# <div class="alert alert-info">
# <strong>COMPLETAR MARCO TEÓRICO!!!!!</strong>
# </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Propuesta</h1> </center> 

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 1.- Dataset

# <div class="alert alert-info">
# 
#     
#    Para poder tener el  <strong>Datset</strong> hay que recolectar información con una encuenta elaborada por nosotros.
#     
# </div>

# #### Encuesta ejemplo:

# La encuesta la realizamos en Google-Form donde se solicitara escoger un Dibujo Animado
# - Donde si escoge 1 es el que menos le gusta hasta 5 que es el que mas le gusta (escala de liker)

# ### Formulario de Google (Preguntas)
# 30 lugares increíbles para visitar en Perú
# 1. Machu Picchu
# 2. Cusco
# 3. La fortaleza de Sacsayhuamán
# 4. Maras y Moray
# 5. Ollantaytambo
# 6. Písac
# 7. Choquequirao
# 8. Monasterio de San Francisco 
# 9. Museo Larco
# 10. Pachacámac
# 11. Líneas de Nazca
# 12. Hacer el tour de tubulares en la Huacachina
# 13. La Reserva nacional de Paracas
# 14. Convento de Santa Catalina
# 15. Cañón del Colca
# 16. Lago Titicaca
# 17. Fortaleza de Kuélap
# 18. Catarata de Gocta
# 19. Mausoleos de Revash
# 20. Parque nacional de Huascarán
# 21. Chavín de Huantar
# 22. Caral
# 23. Trujillo
# 24. Chan Chan
# 25. Huaca de la Luna
# 26. Museo Tumbas Reales de Sipán
# 27. Los Manglares de Tumbes
# 28. Ayacucho
# 29. La Reserva de Pacaya Samiria
# 30. El Parque nacional del Manu

# ### Formulario de Google (Imagenes)

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


m_corrpanda = np.round(m_corrpanda, 
                       decimals = 1)  
  
m_corrpanda


# In[ ]:


m_corrpanda


# ## Mayor Numero

# In[ ]:


m_corrpanda[m_corrpanda>=1] = -0.4
m_corrpanda


# In[ ]:


m_corrpanda.max()


# In[ ]:


x = m_corrpanda[m_corrpanda.columns[0:]].to_numpy()
print(x)


# In[ ]:


# Inicializar y asumir que tanto el mayor como el menor están en el primer elemento; solo para inicializar
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


pip install matplotlib


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.heatmap(data=m_corrpanda)
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


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# In[ ]:


print(m[0])
m_corr_mio[0]


# In[ ]:


## Grafica de calor mío
sns.heatmap(m_corr_mio)
plt.show


# <center> <h1>Conclusiones</h1> </center> 

#  <div class="alert alert-info">
#     
#    - ¿Se valido o no los resultados?
#    - Los resultados Validados son:
#    - ¿Es efectivo el metodo de correlación de pearson?
#    - Correlación de Pearson y Regresión Lineal, ¿cual es su relación?
#     
#  </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# 
# <center> <h1>RESUMEN - Investigación Formativa - Proyecto Final</h1> </center> 

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ### Temas

#  1. Musica
#  2. Peliculas
#  3. Comida
#  4. Lugares que deseo conocer
#  5. Obras de Arte

# ### Procedimiento

# #### 1.- `Realizar Encuesta` EN GOOGLE FORMS casillas no obligatorias
# #### 2.- `Editar archivo plantilla - Jupyter Notebook con los resultados obtenidos` 
#     Avance 1:
#       - Resultados automaticos con funcion de busqueda de 2 valores maximos.
#       - Validación Matrix de Correlación 
#       - Gráfica de calor de Matrix de Correlación
#       - Caso Netflix - Imputar Valores NaN con ¿?
# #### 3.- `Programar con Python pagina web APP STREAMLIT donde presenta el procedimiento y resultados ` 
#     Avance 2: 
#       - Investigación STREAMLIT
#       - APP web interactiva
#       - Dashboard
#       - Mismos datos interactivos de archivo Jupyter Notebook
# #### 4.- `Sustentación de Resultados`( Investigación Formativa)
# 
# 

# ## CASO Netflix
# ### Inputación de `NaN`

# |Estudiante   |	Pelicula 1	  |    Pelicula 2 |     Pelicula 3|   Pelicula 4  |
# |:-----------:|:-------------:|:-------------:|:-------------:|:-------------:|
# |Oscar        |          4    |       NaN        |        5      |        NaN       |
# |Andrea       |        2      |       1       |        NaN       |      5        |
# |Juan         |    5          |       NaN        |   3           |       2       |
# 

# |             |	Oscar	      |    Andrea     |     Juan     |
# |:-----------:|:-------------:|:-------------:|:------------:|
# |Oscar        |           1   |    __0,33__   |  0,30        |
# |Andrea       |    __0,33__   |       1       |   0,19       | 
# |Juan         |    0,30       |       0,19    |  1           | 
# 

# Podemos observar que es mas probable recomendar a __`Oscar`__ la __`Pelicula 4`__ por los gusto de __`Andrea`__ 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# ## Referencia

# - __Profesor de Matematicas__: `John Gabriel Muñoz Cruz`
# https://www.linkedin.com/in/jgmc
# https://parzibyte.me/blog/2020/11/27/mayor-menor-matriz-python/
# 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)
