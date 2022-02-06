import os
from scipy import ndimage
from scipy import misc
import imageio
import matplotlib.pyplot as plt
import image_handler

imageHandler = image_handler.ImageHandler()
imageBinary = imageHandler.loadRGBImageBinary("atm256color.jpg")
print("imageBinary[0][0]", imageBinary[0][0])

encryptedImage = imageHandler.processImage_AES_A51(imageBinary, "ENCRYPT", "AES_A51")
print("encryptedImage[0][0]", encryptedImage[0][0])

reconstructedImageEncrypted = imageHandler.reconstructImage(encryptedImage)
print("reconstructedImageEncrypted[0][0]", reconstructedImageEncrypted[0][0])

plt.imshow(reconstructedImageEncrypted)
plt.show()

decryptedImage = imageHandler.processImage_AES_A51(encryptedImage, "DECRYPT", "AES_A51")
print("decryptedImage[0][0]", decryptedImage[0][0])

reconstructedImageDecrypted = imageHandler.reconstructImage(decryptedImage)
print("reconstructedImageDecrypted[0][0]", reconstructedImageDecrypted[0][0])

plt.imshow(reconstructedImageDecrypted)
plt.show()

originalImage = imageio.imread("atm256color.jpg")
#print(originalImage - reconstructedImageEncrypted)
print("psnr", imageHandler.psnr(originalImage, reconstructedImageEncrypted))
