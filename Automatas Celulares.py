# Automatas Celulares
# El juego de la vida de Conway
# Tamaño tablero 800 x 600

# Descripción del juego
# 1. Una célula muerta con exactamente tres células vecinas vivas se convierte en una célula viva. Esto se llama nacimiento.
# 2. Una casilla con dos o tres vecinos vivos permanece viva (se dice que sobrevive).
# 3. En cualquier otro caso, la célula morirá ya sea por superpoblación (si tiene más de tres vecinos vivos) o de soledad/aislamiento (si tiene menos de dos vecinos vivos).

# Célula viva será X y una muerta " "

# librerias

# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt

#configuracion necesaria de pyplot para ver las imagenes en escala de blanco negro
color='white'
plt.rcParams['image.cmap'] = color


# comando de Jupyter para que las imagenes se muestren automaticamente 

#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np

#tamaño de las matrices a visualizar
alto=600
ancho=800
size=(alto,ancho)

# IMAGEN BLANCA
# Una matriz de unos. 
imagen_blanca = np.ones(size)

#visualizamos la matriz
#Se ve como una imagen blanca, ya que todos los elementos (pixeles) tienen intensidad 1
plt.imshow(imagen_blanca,vmin=0,vmax=1)

#creamos otra figura para mostrar la imagen (sino el proximo imshow sobreescribe al anterior)
plt.figure()
# IMAGEN GRIS
# Una matriz con valor 0.5 en todos sus elementos 
imagen_gris = np.ones(size)*0.5
#visualizamos la matriz
#Se ve como una imagen gris, ya que todos los elementos (pixeles) tienen intensidad 0.5
plt.imshow(imagen_gris,vmin=0,vmax=1)
#plt.image(AxesImage , 0x7f24680ea9b0)
#from imread import imread, imsave
#from mahotas import gaussian_filter
 #image = imread('celula.jpg')
#from image import io
#image= imread('celula.jpg')
# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1
print("- Dimensiones de la imagen:")
#print(image.shape)
#plt.imshow(image,vmin=0,vmax=1))
