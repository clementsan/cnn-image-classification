from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import scipy
import scipy.ndimage as scind
import os


def read_img(file_name):

	img = scind.imread(file_name)
	#print(img.shape)
	img = img[:-63,...]
	#print(img.shape)

	return img


def rgb2gray(img):

	R = np.copy(img[:,:,0])
	G = np.copy(img[:,:,1])
	B = np.copy(img[:,:,2])
	
	gray = 0.2989 * R + 0.5870 * G + 0.1140 * B 

	return gray
	

# Random extracting patch region of image
def patchData(img, w = 400, h = 400):

	#w = int(w); h = int(h)
	Limit_x = img.shape[0] - w
	Limit_y = img.shape[1] - h

	pImg = np.zeros((w,h))
	
	x = np.random.randint(0, Limit_x)
	y = np.random.randint(0, Limit_y)

	print(x, y, x+w, y+h)

	pImg = np.copy(img[x:x+w,y:y+h])
	
	return pImg

# Random extracting patch region of image
def patchData2(img, w = 400, h = 400):

	#w = int(w); h = int(h)
	Limit_x = img.shape[0] - w
	Limit_y = img.shape[1] - h

	pImg = np.zeros((w,h))
	
	x = np.random.randint(0, Limit_x)
	y = np.random.randint(0, Limit_y)

	#print(x, y, x+w, y+h)

	pImg = np.copy(img[x:x+w,y:y+h])
	
	return pImg, int(x), int(y)

def mosaicData(img, index, w = 400, h = 400):

	if (index== 0):
		Begin_x = 0
		End_x = h
		Begin_y = 0
		End_y = w
	elif (index== 1):
		Begin_x = 0
		End_x = h
		Begin_y = w
		End_y = 2*w
	elif (index== 2):
		Begin_x = h
		End_x = 2*h
		Begin_y = 0
		End_y = w
	elif (index== 3):
		Begin_x = h
		End_x = 2*h
		Begin_y = w
		End_y = 2*w

	#print(Begin_x, End_x, Begin_y, End_y)

	pImg = np.copy(img[Begin_x:End_x,Begin_y:End_y])

	#print(pImg.shape)

	return pImg

def mosaicData_9blocks(img, index, w = 300, h = 300):

	if (index== 0):
		Begin_x = 0
		End_x = h
		Begin_y = 0
		End_y = w
	elif (index== 1):
		Begin_x = 0
		End_x = h
		Begin_y = w
		End_y = 2*w
	elif (index== 2):
		Begin_x = 0
		End_x = h
		Begin_y = 2*w
		End_y = 3*w
	elif (index== 3):
		Begin_x = h
		End_x = 2*h
		Begin_y = 0
		End_y = w
	elif (index== 4):
		Begin_x = h
		End_x = 2*h
		Begin_y = w
		End_y = 2*w
	elif (index== 5):
		Begin_x = h
		End_x = 2*h
		Begin_y = 2*w
		End_y = 3*w
	elif (index== 6):
		Begin_x = 2*h
		End_x = 3*h
		Begin_y = 0
		End_y = w
	elif (index== 7):
		Begin_x = 2*h
		End_x = 3*h
		Begin_y = w
		End_y = 2*w
	elif (index== 8):
		Begin_x = 2*h
		End_x = 3*h
		Begin_y = 2*w
		End_y = 3*w

	#print(Begin_x, End_x, Begin_y, End_y)

	pImg = np.copy(img[Begin_x:End_x,Begin_y:End_y])

	#print(pImg.shape)

	return pImg

def mosaicData_Overlap(img, w = 400, h = 400, Overlap_w = 100, Overlap_h = 100):

	# Block
	Begin_h = 0
	Begin_w = 0

	# Block limit
	End_h = Begin_h + h
	End_w = Begin_w + w

	pImg_Array = []
	Iteration_w = 0
	Nb_Iterations = 0

	while End_w <= (img.shape[1]):
		#print("Iteration_w: ",Iteration_w)

		Begin_h = 0
		End_h = Begin_h + h
		Iteration_h = 0
		while End_h <= (img.shape[0]):
			#print("\tIteration_h: ",Iteration_h)
			#print("\t\t[Begin_h:End_h,Begin_w:End_w]: ",Begin_h,End_h,Begin_w,End_w)
			# Copy Block
			pImg = np.copy(img[Begin_h:End_h,Begin_w:End_w])
			# Append block to array
			pImg_Array.append(pImg)

			# Increase block by overlap
			Begin_h = Begin_h + Overlap_h
			End_h = Begin_h + h
			Iteration_h += 1
			Nb_Iterations += 1

		# Increase block by overlap
		Begin_w = Begin_w + Overlap_w
		End_w = Begin_w + w
		Iteration_w += 1

	#print("\nNb_Iterations: ",Nb_Iterations)
	return pImg_Array


# Random extracting patch region of image
def colorTestImage(img, x, y, w = 400, h = 400):
  img[x:x+w,y:y+h] = 255

  return img
