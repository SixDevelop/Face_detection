from webbrowser import get
from matplotlib import pyplot as plt
import cv2 as cv2
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from scipy.fftpack import dct
path_to_images = 'task2/ORLimages/'

def get_histogram(image, param = 30):
    hist, bins = np.histogram(image, bins=np.linspace(0, 1, param))
    return [hist, bins]

def get_dft(image, mat_side = 13):
    f = np.fft.fft2(image)
    f = f[0:mat_side, 0:mat_side]
    return np.abs(f)

def get_dct(image, mat_side = 13):
    c = dct(image, axis=1)
    c = dct(c, axis=0)
    c = c[0:mat_side, 0:mat_side]
    return c

def get_gradient(image, n = 2):
    n=n-1
    shape = image.shape[0]
    i, l = 0, 0
    r = n
    result = []

    while r <= shape:
        window = image[l:r, :]
        result.append(np.sum(window))
        i += 1
        l = i * n
        r = (i + 1) * n
    result = np.array(result)
    return result

def get_scale(image, scale = 0.35):
	#image = image.astype('float32') 
	h = image.shape[0]
	w = image.shape[1]
	new_size = (int(h * scale), int(w * scale))
	return cv2.resize(image, new_size, interpolation = cv2.INTER_AREA)

def get_faces():
	data_images = fetch_olivetti_faces()
	data_target = data_images['target']
	data_images=data_images['images']
	return [data_images, data_target]

