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

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image_ = img_as_float(io.imread(args["image"]))
len_ori, width_ori, channel_ori = image_.shape

#because the original image is too big, my laptop cannot handle this, so I divide the whole picture into several part(into grid).
num_row = 6 #this is the number of the row of the grid
num_col = 6 #this is the number of the colume of the grid, the recommend number is the (width of the picture / width of a single grass)
numSegments = 260



image_ = imresize(image_, 0.5, interp='nearest')
mask = np.zeros(image_.shape[:-1], dtype = np.int32)
len, width, channel = image_.shape
print(str("the rescaled image size is ") + str(len) + " " + str(width) + " " + str(channel))

row_len = len/num_row + 1
col_len = width/num_col + 1
croped = []

test_size = 0
tot = 0

for cur_row in range(num_row):
	for cur_col in range(num_col):
		
		x1 = cur_row * row_len
		x2 = (cur_row + 1) * row_len
		y1 = cur_col * col_len
		y2 = (cur_col + 1) * col_len
		croped += [[x1, x2, y1, y2]]
		
		image = image_[x1: x2, y1: y2, :]
		
		print(image.shape)
		'''test_size += 1
		if test_size < 9:
			break;
		if test_size > 10:
			break;
		'''
		
		segments = slic(image, n_segments = numSegments, sigma = 5)#this is the slic method

		#segments = quickshift(image)#this is the sift method
		
		segments += tot * numSegments
		tot += 1
		print(str(100.0 * tot/(num_row * num_col)) + "%")
		mask[x1: x2, y1: y2] = segments
		
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
'''fig = plt.figure("Superpixels --  segments")
ax = fig.add_subplot(1, 1, 1)

ax.imshow(mark_boundaries(image_, mask))
plt.savefig('test.png')
plt.axis("off")
plt.show()'''
