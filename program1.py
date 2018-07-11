# Prozentausgabe

import cv2

path='location_of_images'
im1 = cv2.imread('3.jpg',0)
hist1 = cv2.calcHist([im1],[0],None,[256],[0,256])

im2 = cv2.imread('2.jpg',0)
hist2 = cv2.calcHist([im2],[0],None,[256],[0,256])

a=cv2.compareHist(hist1,hist2,cv2.HISTCMP_BHATTACHARYYA)

print "Sie sind zu " + str(a) + " % unterschiedlich"

if a < 0.5:
	print "Also kann man davon ausgehen, dass sie vom gleichen Geschlecht sind"
elif a == 0.5:
        print "Kategorie undefined."
else :
	print "Also kann man davon ausgehen, dass sie nicht vom gleichen Geschlecht sind"
	
# Größe vom Bild wird ausgegeben
img = cv2.imread("3.jpg", cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)

# resize image, Größe der beiden Bilder muss bei der unteren Methode dieselbe sein
# Bildausgabe mus geschlossen werden, damit result.jpg erstellt wird
width = 300
height = 500
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite('3.jpg',resized) 
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Vergleich mit anschließender Bildausgabe als result.jpg

import numpy as np
image1 = cv2.imread("3.jpg")
image2 = cv2.imread("2.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result is True:
    print "Die Bilder sind gleich"

else: cv2.imwrite("result.jpg", difference) # Bildausgabe
print "Die Unterschiede kann man in result.jpg einsehen"
