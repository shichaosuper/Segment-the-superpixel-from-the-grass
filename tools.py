from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage import transform  
from skimage.util import img_as_float
from skimage import io, data
import matplotlib.pyplot as plt
import argparse
import numpy as np
import os
from scipy.misc import imresize
from scipy import ndimage as ndi
from scipy.misc import imsave
from read_mask import read_mask as readm
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image_ = img_as_float(io.imread(args["image"]))
len_ori, width_ori, channel_ori = image_.shape

numSegments = 400# number of the segmentation seed


image_ = imresize(image_, 0.5, interp='nearest')
mask = np.zeros(image_.shape[:-1], dtype = np.int32)
len, width, channel = image_.shape
print(str("the rescaled image size is ") + str(len) + " " + str(width) + " " + str(channel))

test_size = 0
find_corner = readm(args["image"][:-4])
mask_pos, resized_row, resized_col = find_corner._find_corner()
print(resized_row, resized_col)
factor_row = len / resized_row
factor_col = width / resized_col

tot = 0

for area in mask_pos:

	print("processing the number " + str(int(tot/2)+1) + " grass")
	row_min, row_max, col_min, col_max = area
	row_min -= 4
	row_max += 4
	col_min -= 1
	col_max += 1
	row_min *= factor_row
	row_max *= factor_row
	col_min *= factor_col
	col_max *= factor_col
	
	
	x1 = max(row_min - 3, 0)
	x2 = min(row_max + 3, len)
	x_12 = (x1 + x2) /2
	y1 = max(col_min - 3, 0)
	y2 = min(col_max + 3, width)
	
	image = image_[x1: x_12, y1: y2, :]
	
	print("grass size " + str(image.shape))
	segments = slic(image, n_segments = numSegments, sigma = 7)#this is the slic method

	#segments = quickshift(image)#this is the sift method
	
	
	
	segments += tot * numSegments
	tot += 1
	mask[x1: x_12, y1: y2] = segments
	
	
	image = image_[x_12: x2, y1: y2, :]
	
	#print("grass size " + str(image.shape))
	segments = slic(image, n_segments = numSegments, sigma = 7)#this is the slic method

	#segments = quickshift(image)#this is the sift method
	
	
	
	segments += tot * numSegments
	tot += 1
	mask[x_12: x2, y1: y2] = segments
	
mask = ndi.zoom(mask, 2, order=0)

np.save(args["image"]+".npy", mask)
image_ = transform.rescale(image_, 2)

		#io.imsave("superpixel" + str(numSegments) + "_" + args["image"], segments)
	 
		#fig = plt.figure("Superpixels --  segments"+str(x1)+str(x2)+str(y1)+str(y2))
		#ax = fig.add_subplot(1, 1, 1)
		#ax.imshow(mark_boundaries(image, segments))
		#plt.axis("off")
		#print(np.max(mask))
marked_pic = mark_boundaries(image_, mask)
imsave(args["image"] + "_superpixel.png", marked_pic)