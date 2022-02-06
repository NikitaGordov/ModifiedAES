import os
import pyaes
from scipy import ndimage
from scipy import misc
import imageio
import matplotlib.pyplot as plt
import image_handler
import numpy as np
import cv2
from PIL import Image

imageHandler = image_handler.ImageHandler()
imageBinary = imageHandler.loadRGBImageBinary("atm256color.jpg")
print("imageBinary[0][0]", imageBinary[0][0])

encryptedImage = imageHandler.processImage_AES_A51(imageBinary, "ENCRYPT", "AES")
print("encryptedImage[0][0]", encryptedImage[0][0])

reconstructedImageEncrypted = imageHandler.reconstructImage(encryptedImage)
print("reconstructedImageEncrypted[0][0]", reconstructedImageEncrypted[0][0])

plt.imshow(reconstructedImageEncrypted)
plt.show()

decryptedImage = imageHandler.processImage_AES_A51(encryptedImage, "DECRYPT", "AES")
print("decryptedImage[0][0]", decryptedImage[0][0])

reconstructedImageDecrypted = imageHandler.reconstructImage(decryptedImage)
print("reconstructedImageDecrypted[0][0]", reconstructedImageDecrypted[0][0])

plt.imshow(reconstructedImageDecrypted)
plt.show()
originalImage = imageio.imread("atm256color.jpg")
#print(originalImage - reconstructedImageEncrypted)
imageio.imwrite("temp.jpg", reconstructedImageEncrypted)
print("psnr", imageHandler.psnr(originalImage, reconstructedImageEncrypted))


#print(np.asarray(reconstructedImageEncrypted, dtype="int32"))
#imageHandler.myHistCalc(imageio.imread("temp.jpg"))
#imageHandler.myHistCalc(originalImage)

#plt.imshow(imageHandler.calcEntropy(imageio.imread("temp.jpg")))
#plt.show()

#print("correlation", imageHandler.calcCorrelation(originalImage, reconstructedImageEncrypted))