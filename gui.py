#tkinter для интерфейса
from tkinter import filedialog
from tkinter import *
#библиотека для инпут аут изображений
from PIL import ImageTk, Image
####
import os
import pyaes
from scipy import ndimage
from scipy import misc
import imageio
import matplotlib.pyplot as plt
import image_handler
#математическая библиотека 
import numpy as np
#тут разметка интерфейса
root = Tk()
root.title("Проект")
root.geometry('1080x720')

def browsefunc():
	global criptat
	filename = filedialog.askopenfilename()  #browse dialog
	im = Image.open(filename) #deschidem imaginea
	h = panel.winfo_height() # label's current height
	w = panel.winfo_width() # label's current width
	#print(h)
	#print(w)
	#w, h = si.size  #Luam dimensiunea imaginii
	#si = si.resize((h,w))
	#print(im)
	ss = ImageTk.PhotoImage(im)
	panel.image=ss # keeping a reference!!
	panel.configure(image=ss)
	global imageHandler
	imageHandler = image_handler.ImageHandler()
	global imageBinary
	imageBinary = imageHandler.loadRGBImageBinary(filename)
	global original
	original = imageio.imread(filename)
	criptat = False
    
def criptAES():
	global criptat
	global imageHandler
	global encryptedImage
	global original
	
	if( criptat == True ):
		return
	
	encryptedImage = imageHandler.processImage_AES_A51(imageBinary, "ENCRYPT", "AES")
	reconstructedImageEncrypted = imageHandler.reconstructImage(encryptedImage)
	
	criptat = True
	
	psnr = imageHandler.psnr(original, reconstructedImageEncrypted)
	psnrValLbl.config(text = psnr)
	
	#corr = imageHandler.calcCorrelation(original, reconstructedImageEncrypted)
	#corrValLbl.config(text = corr)
	
	imageio.imwrite("temp.jpg", reconstructedImageEncrypted)
	
	f, axarr = plt.subplots(2,3)
	axarr[0,0].imshow(original)
	axarr[0,0].set_title("Оригинальная")
	axarr[0,1].plot(imageHandler.myHistCalc(original))
	axarr[0,1].set_title("Гистограма")
	axarr[0,2].imshow(imageHandler.calcEntropy(original))
	axarr[0,2].set_title("Энтропия")
	
	axarr[1,0].imshow(reconstructedImageEncrypted)
	axarr[1,0].set_title("Зашифровать")
	axarr[1,1].plot(imageHandler.myHistCalc(imageio.imread("temp.jpg")))
	axarr[1,1].set_title("Гистограма")
	axarr[1,2].imshow(imageHandler.calcEntropy(imageio.imread("temp.jpg")))
	axarr[1,2].set_title("Энтропия")
	
	plt.show()
	
	#plt.imshow(reconstructedImageEncrypted)
	#plt.show()
	
	
	#im = Image.fromarray(reconstructedImageEncrypted)
	
	#print(im)
	
	#ss = ImageTk.PhotoImage(reconstructedImageEncrypted)
	#im2 = Image.new(im.mode, im.size)
	#im2.putdata(reconstructedImageEncrypted)
	#im2 = Image.fromarray(np.uint8(reconstructedImageEncrypted),"L")
	#im2 = Image.fromarray(reconstructedImageEncrypted.T, 'RGB')
	#print(im2)
	#print(encryptedImage)
	#panel.configure(image=reconstructedImageEncrypted)

def decriptareAES():
	global criptat
	global imageHandler
	global encryptedImage
	
	if( criptat == False ):
		return
		
	decryptedImage = imageHandler.processImage_AES_A51(encryptedImage, "DECRYPT", "AES")
	reconstructedImageDecrypted = imageHandler.reconstructImage(decryptedImage)
	
	criptat = False
	
	plt.imshow(reconstructedImageDecrypted)
	plt.show()

def cryptMAES():
	global criptat
	global imageHandler
	global encryptedImage
	global original
	
	if( criptat == True ):
		return
	
	encryptedImage = imageHandler.processImage_AES_A51(imageBinary, "ENCRYPT", "A51")
	reconstructedImageEncrypted = imageHandler.reconstructImage(encryptedImage)
	
	criptat = True
	
	psnr = imageHandler.psnr(original, reconstructedImageEncrypted)
	psnrValLbl.config(text = psnr)
	
	#corr = imageHandler.calcCorrelation(original, reconstructedImageEncrypted)
	#corrValLbl.config(text = corr)
	
	imageio.imwrite("temp.jpg", reconstructedImageEncrypted)
	
	f, axarr = plt.subplots(2,3)
	axarr[0,0].imshow(original)
	axarr[0,0].set_title("Оригинальная")
	axarr[0,1].plot(imageHandler.myHistCalc(original))
	axarr[0,1].set_title("Гистограма")
	axarr[0,2].imshow(imageHandler.calcEntropy(original))
	axarr[0,2].set_title("Энтропия")
	
	axarr[1,0].imshow(reconstructedImageEncrypted)
	axarr[1,0].set_title("Зашифровать")
	axarr[1,1].plot(imageHandler.myHistCalc(imageio.imread("temp.jpg")))
	axarr[1,1].set_title("Гисторграма")
	axarr[1,2].imshow(imageHandler.calcEntropy(imageio.imread("temp.jpg")))
	axarr[1,2].set_title("Энтропия")
	
	plt.show()
	
	#plt.imshow(reconstructedImageEncrypted)
	#plt.show()

def decryptMAES():
	global criptat
	global imageHandler
	global encryptedImage
	
	if( criptat == False ):
		return
		
	decryptedImage = imageHandler.processImage_AES_A51(encryptedImage, "DECRYPT", "A51")
	reconstructedImageDecrypted = imageHandler.reconstructImage(decryptedImage)
	
	criptat = False
	
	plt.imshow(reconstructedImageDecrypted)
	plt.show()


criptat = False
	
# Code to add widgets will go here...
browseBtn = Button(root, text ="Загрузить изображение", command = browsefunc)
criptAesBtn = Button(root, text = "Зашифровать MAES", command = criptAES)
decriptAesBtn = Button(root, text = "Расшифровать MAES", command = decriptareAES)
cryptMAESBtn = Button(root, text = "Зашифровать AES", command = cryptMAES)
decryptMAESBtn = Button(root, text = "Расшифровать AES", command = decryptMAES)

psnrLbl = Label(root, text="Сигнал/Шум: ")
#corrLbl = Label(root, text="CORR: ")
psnrValLbl = Label(root)
#corrValLbl = Label(root)
panelFrame = Frame(root)
panel = Label(panelFrame, height="512", width="512")

browseBtn.grid(row=0, column=0)
criptAesBtn.grid(row=1, column=0)
decriptAesBtn.grid(row=1, column=1)
cryptMAESBtn.grid(row=2, column=0)
decryptMAESBtn.grid(row=2, column=1)

psnrLbl.grid(row=4, column=0)
psnrValLbl.grid(row=4, column=1)
#corrLbl.grid(row=5, column=0)
#corrValLbl.grid(row=5, column=1)

panelFrame.grid(row=6, column=2)
panel.pack()

root.mainloop()