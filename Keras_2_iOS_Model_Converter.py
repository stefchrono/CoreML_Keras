import coremltools
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.models import load_model
import keras


def convert_model(model):
	coreml_model = coremltools.converters.keras.convert(model,input_names=['image'],image_input_names='image')
	coreml_model.author = 'NAME'
	coreml_model.short_description = 'Read a handwritten digit.'
	coreml_model.input_description['image'] = '28x28 pixel image'
	coreml_model.output_description['output1'] = 'One-hot Multiarray'
	coreml_model.save('/path/to/Keras_Digit_Recognizer.mlmodel')


import os.path
if os.path.isfile('/path/to/Digit_Recognizer.h5'):
	model = load_model('/path/to/Digit_Recognizer.h5')
	convert_model(model)
else:
	print('no model found')
