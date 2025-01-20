"""
💻 PROCESAMIETNO DE IMAGENES CON OPENCV

📌 Descripción: Diseña un programa que cargue imágenes, aplique transformaciones básicas como redimensionado, 
cambio de color, detección de bordes (Canny) y filtrado (Gaussian blur).

📌 Librerías: OpenCV, NumPy.

📌 Objetivo: Comprender la manipulación de imágenes en matrices.

"""

import cv2
import math
import glob
import numpy as np
import Images_Module as module

resized_path = "D:/Programacion/Images/Resized/"
colored_path = "D:/Programacion/Images/Colored/"
canny_path = "D:/Programacion/Images/Canny/"
gaussian_blur_path = "D:/Programacion/Images/Gaussian_Blur/"

image_path = glob.glob("D:/Programacion/Images/*.*")
print("> Filtering images...")
image_path = module.filter(image_path)# -> Path where we get only jpeg, jpg and png format

for image in image_path:
    
    name = module.search_name_format(image)
    image = cv2.imread(image)# -> Image = Matriz nxnxm; where m is the number of channels.
    
    if(image.ndim == 3):# -> ndim return the number of channels in the image. If ndim returns 1 -> Gray scale.
        
        print(f"\t> {name}")

        # RESIZED #
        (height, width, channels) = image.shape
        new_height = math.trunc(0.5*height)
        new_width = math.trunc(0.5*width)

        resized_image = cv2.resize(image, (new_width, new_height))
        cv2.imwrite(f"{resized_path}{name}", resized_image)

        print(f"\t\t> {name} -> Resized to 50% completed.")

        # COLOR CHANGE -> GRAY SCALE #
        """
            CV2 assign the color channels in the following order:
            image[:,:,0] -> Blue  B
            image[:,:,1] -> Green G
            image[:,:,2] -> Red   R
        """
        
        r = resized_image[:,:,2]
        g = resized_image[:,:,1]
        b = resized_image[:,:,0]

        gray_scale_image = 0.299*r + 0.587*g + 0.114*b

        cv2.imwrite(f"{colored_path}{name}", gray_scale_image)
        """
            gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{colored_path}{name}", gray)
        """

        print(f"\t\t> {name} -> Color Change completed.")

        # EDGE DETECTION -> CANNY #       
        """
            METODO 1:

            gray_scale_image_U8 = cv2.convertScaleAbs(gray_scale_image)# -> Convert image to 8 bits format.
            low_threshold = 100
            high_threshold = 250
            canny = cv2.Canny(gray_scale_image_U8, low_threshold, high_threshold)

            cv2.imwrite(f"{canny_path}{name}", canny)
        """

        """ METODO 2 """
        edge_kernel = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
        canny = cv2.filter2D(gray_scale_image, -1, edge_kernel)# -> Convolution function WITH REFLECTED PADDING. -1 to use the same bit depth.
        
        max_value = canny.max()#-> Max gradient in the image
        canny_n = (canny / max_value) * 255# -> Normalization

        cv2.imwrite(f"{canny_path}{name}", canny_n)

        print(f"\t\t> {name} -> Edge Detection completed.")

        # FILTERING -> GAUSSIAN BLUR #

        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        gaussian_kernel = (1/16) * kernel
        blur = cv2.filter2D(resized_image, -1, gaussian_kernel)
        cv2.imwrite(f"{gaussian_blur_path}{name}", blur)

        print(f"\t\t> {name} -> Gaussian Blur completed.")

print("\t> Filtering finished.")


