# TAE_T3

¡Bienvenido! En este repositorio usted podrá encontrar lo relacionado con la realización de un modelo de clasificación para determinar si una persona retratada en una fotografía **porta gafas o no**, el cual fue desarrollado a partir de **redes neuronales convolucionales.** A continuación se describen algunos archivos de este repositorio, de manera que usted pueda ubicar fácilmente los documentos que aquí reposan.

1. *Gafas.* Carpeta en la que almacen documentos importantes para la creación del informe técnico de este proyecto
  1.1. **Entre_Procesado.jpg.** Imagen de ejemplo del conjunto de entrenamiento después de procesar, es decir, haciendo escalado y llevándolo a escala de grises.
  1.2. **Entre_SinProcesar.jpg.** Imagen de ejemplo del conjunto de entrenamiento sin procesar, es decir, tal y como fue obtenida de la red.
  1.3. **Gajas.Rproj.** Archivo del lenguaje de programación _R_ que permite la existencia de un proyecto que abarque todos estos documentos dentro de _R Studio_ para poder generar el reporte técnico.
  1.4. **Informe_Tecnico.Rmd.** Documento de _R Markdown_ en el que se escribe el informe técnico que va a ser entregado.
  1.5. **Infore_Tecnico.html.** Documento _HTML_ legible para poder observar el informe técnico. Este documento puede ser visualizado y leído por cualquier persona al ser publicado en _R Pubs_.
  1.6. **MatrizC.png.** Fotografía con la matriz de confusión obtenida en el conjunto de validación empleada para poder adjuntarla en el informe técnico.
  1.7. **ModelAccuracy.png.** Imagen que muestra la exactitud del modelo en los conjuntos de entrenamiento y de validación.
  1.8. **ModelLoss.png.** Imagen empleada para determinar la pérdida del modelo en los conjuntos de entrenamiento y validación para ser adjuntada en el informe técnico.
  1.9. **ProcesamientoDos.py.** Programa de _Python_ que toma las imágenes del conjunto de entrenamiento obtenidas de _Kaggle_ para pasarlas a escala de grises y reescalarlas a unas dimensiones estándar.
  1.10. **ProcesamientoDos.py.** Programa de _Python_ que toma las imágenes del CMU de la Universidad de California en Irvine (UCI) para reescalarlas a unas dimensiones estándar.
  1.11. **ProcesamientoUno.py.** Programa de _Python_ que toma las imágenes del conjunto de entrenamiento obtenidas de _Google Images_ para pasarlas a escala de grises y reescalarlas a unas dimensiones estándar.
  1.12. **Resultado_Ind.PNG.** Ejemplo del resultado del modelo predictivo con una de las imágenes del conjunto de validación.
  1.13. **Samples-of-CMU-faces-images-dataset.png.** Imagen que agrupa varias imágenes del conjunto de validación para mostrar las diferentes expresiones faciales que pueden existir en este conjunto, en el que se observa como las personas pueden tener o no gafas y diferentes expresiones y orientes del rostro. Se generó para poder ser adjuntada en el informe técnico.
  1.14. **image159.pgm.** Imagen del conjunto de validación empleada para mostrar lo que se realizó con su procesamiento en el archivo _ProcesamientoTres.py_.
  1.15. **image60.pgm.** Imagen del conjunto de validación empleada para mostrar lo que se realizó con su procesamiento en el archivo _ProcesamientoTres.py_.

2. **Modelo_Python.** En esta carpeta se encuentran tres archivos de _Python_ con los que se desarrolla el modelo de clasificación empleando redes neuronales convolucionales. Dichos archivos son:
  2.1. **Modelo_Preddiciones.ipynb.** Este archivo es un _notebook_ en el que se aborda el testeo del modelo que ha sido entrenado con las imágenes del dataset CMU de la base de datos para trabajos con aprendizaje automático de la Universidad de California en Irvine (UCI) y se muestra la matriz de confusión asociada.
  2.2. **Modelo_TAE_Trabajo3.ipynn.** Este archivo es un _notebook_ de _Python_ en los que se explica y se desarrolla el modelo creado para la clasificación de fotografías en función de si las personas retratadas en estas lucen gafas o no.
  2.3. **modelo.h5.** Es un documento que almacena información relacionada con la creación del modelo.
 
