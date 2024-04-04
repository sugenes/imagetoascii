import cv2 as cv
import math
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#изменяем размер нового изображения
def resizeImage(image, new_width = 100):
    old_width = image.shape[0]
    old_height = image.shape[1]
    new_height = math.ceil(new_width * old_height / old_width)
    new_image = cv.resize(image, (new_width, new_height))
    return new_image

#замена пикселей изображения символами ascii
def convertToAscii(image):
    size = image.shape
    temp = ""
    for i in range(size[0]):
        for j in range(size[1]):
            number = math.trunc(image[i, j] / 25)
            temp += ASCII_CHARS[number]
            #Первый вариант замены пикселя символом ascii
            """if image[i, j] >= 0 and image[i, j] <= 10:
                temp += (ASCII_CHARS[0])
            elif image[i, j] > 10 and image[i, j] <= 20:
                 temp +=(ASCII_CHARS[1])
            elif image[i, j] > 20 and image[i, j] <= 30:
                         temp +=(ASCII_CHARS[2])
            elif image[i, j] > 30 and image[i, j] <= 40:
                         temp +=(ASCII_CHARS[3])
            elif image[i, j] > 40 and image[i, j] <= 50:
                         temp +=(ASCII_CHARS[4])
            elif image[i, j] > 50 and image[i, j] <= 60:
                        temp +=(ASCII_CHARS[5])
            else:
                temp +=(ASCII_CHARS[6])"""
        temp +="\n"

    return temp
    
image = cv.imread("D:/Python/ITA/cat.jpg")
#cv.imshow("Old image", image)
#k = cv.waitKey(0)
new_image = resizeImage(image)
grey_image = cv.cvtColor(new_image, cv.COLOR_BGR2GRAY)
#cv.imshow("Display window", grey)
#cv.imshow("New image", new_image)
#k = cv.waitKey(0)
converted_image = convertToAscii(grey_image)
with open("D:/Python/ITA/test.txt", "w", encoding="utf-8") as f:
       f.write(converted_image)
print(converted_image)
