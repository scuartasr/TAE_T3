Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@scuartasr 
scuartasr
/
TAE_T3
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
TAE_T3/Gafas/ProcesamientoTres.py /
@scuartasr
scuartasr Procesamiento - validación
…
Latest commit f49f233 18 minutes ago
 History
 1 contributor
26 lines (17 sloc)  676 Bytes
  
# Procesamiento de las imágenes de la carpeta "Faces"
import cv2 as cv2
import glob
import os

os.mkdir('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Procesadas_Faces/')

images_path = glob.glob('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Faces/*.pgm')

dim = (171, 213)


i = 0

for image in images_path:
    
    img = cv2.imread(image)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    #gray_images = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', resized)
    cv2.imwrite('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Procesadas_Faces/image%02i.pgm' %i, resized)
    i += 1
    cv2.waitKey(600)
    cv2.destroyAllWindows()
    
