import cv2 
import numpy as np

imagen = cv2.imread('Lagartija.jpg')

Canny = cv2.Canny(imagen, 150, 200)
Dialation = cv2.dilate(Canny, kernel, iterations=1)
Eroded = cv2.erode(Dialation,kernel,iterations=1)

ims = cv2.resize(imagen,(200,250))
imgr = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imsr = cv2.resize(imgr,(210,260))
imcd = cv2.resize(Dialation,(220,270))
imd=cv2.rectangle(imagen,(100,900),(500,300),(0,0,255))
imdd = cv2.resize(imd,(150,200))
imcr = cv2.resize(Canny,155,205))
imce = cv2.resize(Eroded,(155,205))

cv2.imshow("Normal", ims)
cv2.imshow("EscalaGris", imsr)
cv2.imshow("BordeadoDialation", imcd)
cv2.imshow("NormalConRectángulo", imdd)
cv2.imshow("BordeadoCanny", imcr)
cv2.imshow("BordeadoEroded", imce)


cv2.waitKey(0)