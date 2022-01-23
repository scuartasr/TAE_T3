# Procesamiento de las imágenes de la carpeta "Kaggle"
import cv2 as cv2
import glob
import os

os.mkdir('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Procesadas_Kaggle/')

images_path = glob.glob('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Kaggle/*.png')

dim = (171, 213)


i = 0

for image in images_path:
    
    img = cv2.imread(image)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    gray_images = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', gray_images)
    cv2.imwrite('C:/Users/lenovo/Documents/TAE/TAE_T3/Gafas/Procesadas_Kaggle/image%02i.png' %i, gray_images)
    i += 1
    cv2.waitKey(600)
    cv2.destroyAllWindows()
    

