import io
import imageio
import os
import pyaes
import A51
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
from scipy import signal


from skimage import data, color
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk


class ImageHandler:
    def __init__(self):
        self.data = []
        self.key = os.urandom(16)
        self.iv = "InitializationVe"
        self.iv = self.iv.encode('utf-8')
        self.byteArgSeed = b'abc'
        self.finalKey = A51.initialize_and_process(
            self.byteArgSeed)  # сид для финального ключа

    def loadRGBImageBinary(self, imageName):
        f = imageio.imread(imageName)
        for i in range(len(f)):
            self.data.append([])
            for j in range(len(f[i])):
                self.data[i].append([])
                temp = b''
                for k in f[i][j]:
                    temp = temp + k
                self.data[i][j] = temp
        return self.data

    # получает бинарное изображение (бинарные массивы) и возвращает изображение
    def reconstructImage(self, imageBinary):
        f = imageBinary
        image = []
        for i in range(len(f)):
            image.append([])
            for j in range(len(f[i])):
                image[i].append([])
                temp = []
                for k in f[i][j]:
                    temp.append(k)
                    # print(k)
                image[i][j] = temp
        return image

    def processImage_AES_A51(self, imageBinary, flag, algType):
        f = imageBinary
        image = []
        aes = pyaes.AESModeOfOperationCTR(self.key)
        for i in range(len(f)):
            image.append([])
            for j in range(len(f[i])):
                image[i].append([])
                # print(f[i][j])
                if flag == "ENCRYPT":
                    if algType == "AES":
                        image[i][j] = aes.encrypt(f[i][j])
                    elif algType == "A51":
                        image[i][j] = A51.encrypt(f[i][j], self.finalKey)
                    elif algType == "AES_A51":
                        image[i][j] = A51.encrypt(
                            aes.encrypt(f[i][j]), self.finalKey)
                elif flag == "DECRYPT":
                    if algType == "AES":
                        image[i][j] = aes.decrypt(f[i][j])
                    elif algType == "A51":
                        image[i][j] = A51.decrypt(f[i][j], self.finalKey)
                    elif algType == "AES_A51":
                        image[i][j] = A51.decrypt(
                            aes.decrypt(f[i][j]), self.finalKey)
        return image

    def psnr(self, img1, img2):
        mse = np.mean((img1 - img2) ** 2)
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

    def myHistCalc(self, img):
        # find frequency of pixels in range 0-255 
        return cv2.calcHist([img],[0],None,[256],[0,256]) 
        
        # show the plotting graph of an image 
        #plt.plot(histr) 
        #plt.show()

    def calcEntropy(self, img):
        rgbImg = img
        grayImg = color.rgb2gray(rgbImg)
        #print(grayImg.shape)  # (667,1000), a 2 dimensional grayscale image
        return entropy(grayImg, disk(10)) 
    
    def calcCorrelation(self, img1, img2):
        #array_a = np.ndarray.flatten(np.array(img1))
        #array_b = np.ndarray.flatten(np.array(img2))
        #results = np.correlate(array_a, array_b)
        #return results
        #arrA = img1[1][0]
        #arrB = img2[1][0]
        return "to do"