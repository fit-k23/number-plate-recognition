import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pytesseract as pt

model = tf.keras.models.load_model('D:\python\Automatic-License-Plate-Detection\800.keras')