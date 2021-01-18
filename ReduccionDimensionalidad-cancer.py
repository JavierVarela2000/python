#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Steve
"""
import sklearn
import mglearn
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA ## Principal Component Analysis 
## PCA Permite reducir el ruido y graficar varias dimensiones en solo 2 dimensiones
## Buscar correlaciones que puedan interesarnos
## %matplotlib inline ## muestra los gráficos ## Para jupiter 
mglearn.plots.plot_pca_illustration()

cancer=load_breast_cancer()
cancer.keys() ## Etiquetas de la variable
cancer.feature_names ## muestra las características del dataset
cancer.feature_names.shape ## muestra el número de características 
## difíciles de graficar
cancer.data ## muestra los datos del dataset 
cancer.data.shape ## muestra el número  de datos del dataset 

## Reducción de la dimensionalidad

pca=PCA(n_components=2) ## definimos el número de ejes
pca.fit(cancer.data) ## se entrena al sistema con la data de cancer

transformada=pca.transform(cancer.data) ## genera una transformación y la pasa 
# a la variable transformada pasando de 30 dimensiones a 2 dimensiones

print(cancer.data.shape) ## muestra de los datos originales; 569 características con 30 dimensiones
print(transformada.shape) ## muestra de los datos reducidos; 569 características con 2 dimensiones
##Bloque
mglearn.discrete_scatter(transformada[:,0],transformada[:,1],cancer.target)  ## Ejecutar en conjunto
plt.legend(cancer.target_names,loc='best') ##Ejecutar en conjunto
plt.xlabel('PCA1') ##Ejecutar en conjunto
plt.ylabel('PCA2') ##Ejecutar en conjunto
##Bloque

from sklearn.preprocessing import MinMaxScaler
escala=MinMaxScaler()
escala.fit(cancer.data)
escalada=escala.transform(cancer.data)
pca.fit(escalada)
transformada=pca.transform(escalada)

##Bloque
mglearn.discrete_scatter(transformada[:,0],transformada[:,1],cancer.target) ##Ejecutar en conjunto
plt.legend(cancer.target_names,loc='best') ##Ejecutar en conjunto
plt.xlabel('PCA1') ##Ejecutar en conjunto
plt.ylabel('PCA2') ##Ejecutar en conjunto

cancer.data ## Información no escalada
escalada ##Información escalada (normalizada)




