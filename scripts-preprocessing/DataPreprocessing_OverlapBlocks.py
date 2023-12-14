#!/usr/bin/env python

#-------------
# Libraries
from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import scipy
import os
import pandas as pd
from shutil import copy

from utils import *

#-------------
# Parameters

CSV_InputFile = '../Database_Query/Database_Query_2018.csv'
CSV_OutputFile = './Dataset_ImageClassification_Overlap-9blocks.csv'


# Warning: full path needed
Database_Dir = '/mnt/database_SEM/2018/'
DataDir = '~/Projects/Project_SEM/Image_Classification/data_Overlap-9blocks/'

Nb_Samples = 20
ROI_Width = 512
ROI_Height = 440
Overlap_Width = int(ROI_Width / 2)
Overlap_Height = int(ROI_Height / 2)

#-------------
# Processing

# Create sample by mosaicing dataset


# Read CSV file
df = pd.read_csv(CSV_InputFile)

# Create new dataframe for analysis
columns = ['Location','Material','Magnification','Resolution','TargetClass','AcquisitionDate']
df2 = pd.DataFrame(columns=columns)

# Iterate over rows
for index, row in df.iterrows():
	FileName = row['Location']
	TargetClass = row['TargetClass']
	#print(row)
	print('\t ImageName: ',FileName)

	DataDir_TargetClass = os.path.join(DataDir,TargetClass)
	if not os.path.exists(DataDir_TargetClass):
		os.makedirs(DataDir_TargetClass)

	img = read_img(FileName)
	img_gray = rgb2gray(img)

	# Generate all block samples
	pimg_gray_Array = mosaicData_Overlap(img_gray, w = ROI_Width, h = ROI_Height, Overlap_w = Overlap_Width, Overlap_h = Overlap_Height)
	Nb_Samples = len(pimg_gray_Array)

	# Generate images
	for i in range(Nb_Samples):
		pimg_gray = pimg_gray_Array[i]

		FileName_RandomSample = FileName.replace(Database_Dir,DataDir_TargetClass + '/')
		FileName_RandomSample = FileName_RandomSample.replace('.tif.tif','.tif')
		FileName_RandomSample = FileName_RandomSample.replace('.tif','_sample_' + str(i+1) + '.tif')
		#print(FileName_RandomSample)

		# Save random sample
		scipy.misc.imsave(FileName_RandomSample, pimg_gray.astype('uint8'))

		row_sample = row.copy()
		row_sample['Location'] = FileName_RandomSample
		#print(row_sample)

		df2 = df2.append(row_sample, ignore_index = True )

# Fill NA values
df2.fillna('NA')

# Display output dataframe
print('\n Output data frame:')
print(df2.head())

# Save new data frame into CSV file
df2.to_csv(CSV_OutputFile, index=False, na_rep = 'NA')
