#!/usr/bin/env python
# coding: utf-8

import streamlit as st
streamlit run [entrypoint file]




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
st.write("* Maras y Moray")
st.write("* Ollantaytambo")
st.write("* Písac")
st.write("* Choquequirao")
st.write("* Monasterio de San Francisco")
st.write("* Museo Larco")
st.write("* Pachacámac")
st.write("* Líneas de Nazca")
st.write("* Hacer el tour de tubulares en la Huacachina")
st.write("* La Reserva nacional de Paracas")
st.write("* Convento de Santa Catalina")
st.write("* Cañón del Colca")
st.write("* Lago Titicaca")
st.write("* Fortaleza de Kuélap")
st.write("* Catarata de Gocta")
st.write("* Mausoleos de Revash")
st.write("* Parque nacional de Huascarán")
st.write("* Chavín de Huantar")
st.write("* Caral")
st.write("* Trujillo")
st.write("* Chan Chan")
st.write("* Huaca de la Luna")
st.write("* Museo Tumbas Reales de Sipán")
st.write("* Los Manglares de Tumbes")
st.write("* Ayacucho")
st.write("* La Reserva de Pacaya Samiria")
st.write("* El Parque nacional del Manu")


st.subheader('Formulario de Google (Imagenes) ')


st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-1.fna.fbcdn.net/v/t1.15752-9/319972017_1608836186213181_9205396135426992499_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeG1-moyJlhpFOXbGMwD-x4OkcxophX-fkKRzGimFf5-Qs3figqHLlPMoOszX4r7-h96pa8UgmR7PrBAIX569oOh&_nc_ohc=uelSnsPmzN4AX8NSB2O&_nc_oc=AQnyuYKSKXfFJltNMs-cwo10AZq0XeM_o0L289fqKG8HomLIIVVnU3AwMwGZjvwV7bQ&tn=JOPy8uCJH79g_CZ7&_nc_ht=scontent.faqp2-1.fna&oh=03_AdSMFff74twcUC13M-ha1UY--pPV0dWOwdKGhY4NmXNt0A&oe=63C7B108)*")

st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-2.fna.fbcdn.net/v/t1.15752-9/319412304_1163347177658514_2115309225890312447_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGi4EbsiOLd-XfCGequ2qUdO0C_zgSa6eM7QL_OBJrp48k9jpDzcrbDjHshPxfKBswDuubnHOjqo2RRDOoGc7ba&_nc_ohc=2xRZVAIxa4wAX-HSnKZ&_nc_ht=scontent.faqp2-2.fna&oh=03_AdSQtgb3MTIv2jwGk9D22fTNGpYmQr5en5CuLONXKQ7rFw&oe=63C7A586)*")

st.subheader('Formulario de Google (Preprocesamiento) ')
st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-3.fna.fbcdn.net/v/t1.15752-9/319560832_838293997284770_8445679745426101639_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHb1Urpa6qNU7Ja01mXc37cINdqrelR1MIg12qt6VHUwvU_WPs_h3t-GhyFRXOynz7wvD-fDGAnXeCyc4QrOwLU&_nc_ohc=0pvs-o-Ls9IAX-JqyyY&tn=JOPy8uCJH79g_CZ7&_nc_ht=scontent.faqp2-3.fna&oh=03_AdR4tCix0puvI8cWuKJXEEQzqYA_-MjHnLv1_q923YYxAQ&oe=63C7B07E)*")




#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd


# In[ ]:

st.subheader('Archivo CSV separado por comas ')
#archivo CSV separado por comas
encuestaLTP = pd.read_csv('LTP.csv')
#leer  lineas
encuestaLTP



# In[ ]:

st.subheader('Cantidad de filas y columnas')
encuestaLTP.shape


# In[ ]:

st.subheader('Mostrando los NaN')
encuestaLTP.dtypes


# In[ ]:

encuestaLTP.isnull().sum()



# In[ ]:
st.subheader('Imputación de NaNs por la media')

for dat in encuestaLTP.columns[1:]:
    encuestaLTP[dat].fillna(encuestaLTP[dat].mean(),inplace=True)
encuestaLTP


# In[ ]:


encuestaLTP.isnull().sum()


st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)*")


st.subheader('2. Correlación de Pearson  (Similitud) ')
# In[ ]:


n = encuestaLTP[encuestaLTP.columns[1:]].to_numpy()
m = encuestaLTP[encuestaLTP.columns[0]].to_numpy()
print(n)
print(m)
n[8]


st.subheader('3. Correlación en Pandas')
# In[ ]:


n.T


# In[ ]:


df = pd.DataFrame(n.T, columns = m)
df


# In[ ]:


m_corrpanda = df.corr()
m_corrpanda


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

st.subheader('4. Matrix de Correlación ')
         
# In[ ]:


m_corrpanda


# In[ ]:


m_corrpanda = np.round(m_corrpanda, 
                       decimals = 4)  
  
m_corrpanda


st.subheader('Mayor Numero')

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

st.subheader('Gráfica de Calor')

st.subheader('Grafica de Calor Propio PANDAS')
st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-2.fna.fbcdn.net/v/t1.15752-9/319840513_2399116010255444_7051683099654578164_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeEGrc4mZ6RttazrP2d7ZoB7UbmWAVdlXMFRuZYBV2VcwVAyZOJXGLfwwTEKf7QiA_T3uFCvQ-tP3NaqTw0ZKYox&_nc_ohc=rzYTJ8x57CoAX8iDBsr&tn=JOPy8uCJH79g_CZ7&_nc_ht=scontent.faqp2-2.fna&oh=03_AdQj55OAGWqjXhu02JYR0gS_QpP5Xx559Vp_XLUIU--eug&oe=63C7E41A)*")

st.subheader('5.- RESULTADOS')

st.write("* 1.dmejiagu@unsa.edu.pe y diquiapazam@unsa.edu.pe  obtienen el PRIMER indice mas alto de similitud *")
#  
st.write("* 2.  dmejiagu@unsa.edu.pe y _fargotem@unsa.edu.pe  obtienen el **SEGUNDO indice mas alto de similitud*")
st.subheader('Se valido o no los resultado')

st.write("*Es validado los resultados con la correlacion de m_corrpanda y la validacion de pandas *")    
st.write("*Los resultados Validados son:*")
st.write("* Los 2 primer mayor resultados*")

st.write("*el mayor es: *") 
st.write("*dpilaresc@unsa.edu.pe      0.8050*")
st.write("*el 2domayor es:*")
st.write("*rramosmont@unsa.edu.pe     0.8050*")
 
st.write("*el 1ermayor es:*")
st.write("*dpilaresc@unsa.edu.pe    0.8049837428908978*")
   
st.write("*el 2domayor es:*")
st.write("*rramosmont@unsa.edu.pe   0.7902805620025483*")
     
st.write("*¿Es efectivo el metodo de correlación de pearson?*")
st.write("* Si porque valor es independiente de cualquier unidad que se utiliza para medir las variables.*")
st.write("*Si la muestra es grande, es más probable la exactitud de la estimación.*")
st.write("*Alguna de las desventajas del coeficiente de correlación son:*")

st.write("*Es necesario las dos variables sean medidas a un nivel cuantitativo continuo.*")
st.write("*La distribución de las variables deben ser semejantes a la curva normal.*")
    
st.write("*Correlación de Pearson y Regresión Lineal, ¿cual es su relación?*")
st.write("* El coeficiente de correlación lineal es una medida de regresión que sirve para establecer una relación lineal entre dos variables. De esta manera, su cálculo permite conocer con exactitud el grado de dispersión de los valores  de una variable en relación con una media para dicha variable.*")
            


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.p
         
st.subheader('Validación de Resultados')

# In[ ]:





# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## Validación - Matrix de Correlación


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

st.subheader('Ordenando la correlación mía con ayuda de pandas')
##Ordenando la correlación mía con ayuda de pandas

corr_mio_ordenada=pd.DataFrame(data=m_corr_mio,columns=m)

corr_mio_ordenada


# In[ ]:


corr_mio_ordenada[corr_mio_ordenada>=0.99] = -0.4
corr_mio_ordenada




corr_mio_ordenada.max().sort_values(ascending=False)

corr_mio_ordenada=pd.DataFrame(data=m_corr_mio,columns=m)


st.subheader('Grafica de Calor Propio')
st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-3.fna.fbcdn.net/v/t1.15752-9/315524988_2000299573502884_9078479069170880252_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGbXntG-rxR00wSqHjiWZhzAsWytH12qCsCxbK0fXaoKwsgHkcpBcK56w1YNRdDYwPQA42ndeCbOR55vPl-3OOp&_nc_ohc=rQBo_SF-VuQAX8Ra29d&_nc_oc=AQkYmNuaCJ5nptCFtczWtuAn0Ds6l4kf0NsWOpFRtqpubeXtSXGqOycNCgCz4JtIHm0&_nc_ht=scontent.faqp2-3.fna&oh=03_AdRNOmlz53GOOzuZf8HAOZpT0K66IR4FbcurUlinMhGEuw&oe=63C7CD1B)*")


st.subheader('Grafica de Calor Propio PANDAS')
st.write("*![que-es-la-regresion-lineal-y-para-que-sirve](https://scontent.faqp2-1.fna.fbcdn.net/v/t1.15752-9/319159407_3230449323885820_2267753677792259507_n.png?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFLn-OlyDpEgCTQ-lRzSkAqiylD1MwMSkKLKUPUzAxKQlUoF06vgyeWpI2vBhdtS0j7rJKiMhVQkqib51u1Owwh&_nc_ohc=uv9fQoET3OAAX-OFHFM&_nc_ht=scontent.faqp2-1.fna&oh=03_AdRYs6gJooAi6T3Ahr03sTLBM5Rb-sY54X5J5nim2zQaRw&oe=63C7CD04)*")


st.subheader('Conclusiones')

st.subheader('Se valido o no los resultado')

st.write("*Es validado los resultados con la correlacion de m_corrpanda y la validacion de pandas *")    
st.write("*Los resultados Validados son:*")
st.write("* Los 2 primer mayor resultados*")

st.write("*el mayor es: *") 
st.write("*dpilaresc@unsa.edu.pe      0.8050*")
st.write("*el 2domayor es:*")
st.write("*rramosmont@unsa.edu.pe     0.8050*")
 
st.write("*el 1ermayor es:*")
st.write("*dpilaresc@unsa.edu.pe    0.8049837428908978*")
   
st.write("*el 2domayor es:*")
st.write("*rramosmont@unsa.edu.pe   0.7902805620025483*")
     
st.write("*¿Es efectivo el metodo de correlación de pearson?*")
st.write("* Si porque valor es independiente de cualquier unidad que se utiliza para medir las variables.*")
st.write("*Si la muestra es grande, es más probable la exactitud de la estimación.*")
st.write("*Alguna de las desventajas del coeficiente de correlación son:*")

st.write("*Es necesario las dos variables sean medidas a un nivel cuantitativo continuo.*")
st.write("*La distribución de las variables deben ser semejantes a la curva normal.*")
    
st.write("*Correlación de Pearson y Regresión Lineal, ¿cual es su relación?*")
st.write("* El coeficiente de correlación lineal es una medida de regresión que sirve para establecer una relación lineal entre dos variables. De esta manera, su cálculo permite conocer con exactitud el grado de dispersión de los valores  de una variable en relación con una media para dicha variable.*")
            
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
