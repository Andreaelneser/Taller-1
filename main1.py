import cv2
import os

path = input("Coloque la dirección de la imagen")
image_name = input("Coloque el nombre de la imagen")
path_file = os.path.join(path, image_name)


class ColorImage:

    def __init__(self):

        self.imagen = cv2.imread(path_file)
        cv2.imshow('Imagen', self.imagen)
        cv2.waitKey(0) #Dejar la imagen en pantalla hasta que se presione cualquier cosa
        cv2.destroyAllWindows()


    def displayProperties(self):

        height, width, channels = self.imagen.shape #Tamaño de la imagen
        print("Alto", height) #Mostrar la altura
        print("Ancho", width) #Mostrar el ancho

    def makeGray(self):

        grayImage = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow('Imagen en grises', grayImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def colorizeRGB(self):

        r = self.imagen.copy()  #Copia de la imagen
        #Canal azul y verde en 0
        r[:, :, 0] = 0
        r[:, :, 1] = 0

        cv2.imshow('R-RGB', r) #Se observa la imagen en color rojo
        cv2.waitKey(0)

    def makeHue(self):

        hsv = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV) #De BGR a HSV
        cv2.imshow('Imagen HSV', hsv) #Imagen HSV
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Se dividen H, S y V y se colocan S y V en 255
        h, s, v = cv2.split(hsv)
        s.fill(255)
        v.fill(255)
        hsv_image = cv2.merge([h, s, v]) #Luego se vuelven a mezclar

        out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR) #Se vuelve a pasar a RGB

        cv2.imshow('Imagen RGB desde HSV', out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


imagen = ColorImage() #Creación de objeto
imagen.displayProperties() #Imagen a método   displayProperties
imagen.makeGray() #Imagen a método makeGray
imagen.colorizeRGB()
imagen.makeHue()

