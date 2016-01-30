# Introducción

Ésta es la implementación del sistema de estabilización de video mediante el 
descriptor ORB. El programa recibe un video, y entrega el video estabilizado en
la misma carpeta.

# Requerimientos
El programa se debe ejecutar usando Python2.7. Las librerías utilizadas son:

* OpenCV 3.0
* Numpy 1.8.2

# Ejecución
Para correr el programa, simplmente ejecutar:

python2.7 videoStab.py

Los parámetros del programa se deben cambiar manualmente en videoStab.py

* videoInPath:  dirección del video a estabilizar
* MATCH_THRES:  umbral de distacia de los calces
* RANSAC_THRES: umbral de RANSAC
* BORDER_CUT:   corte de bordes en el video estabilizado
* FILT:         tipo de filtro (square o gauss)
* FILT_WIDTH:   ancho del filtro
* FILT_SIGMA:   varianza del filtro gaussiano
* FAST:         Si True usa la versión rápida del algoritmo 

Más información leer el informe.
