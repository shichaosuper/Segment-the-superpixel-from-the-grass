# Segment-the-superpixel-from-the-grass

#### It is a tool to generate the segmentation of the sick grass

&#160;

## Requirements(python package)

    scikit-image
    matplotlib
    scipy
    numpy

## Note
&#160;&#160;&#160;&#160;&#160;&#160;&#160;Instead of using the original code, I use the method in the skimage library

&#160;&#160;&#160;&#160;&#160;&#160;&#160;If you want to find the original code, here is the link : &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;http://ivrlwww.epfl.ch/supplementary_material/RK_SLICSuperpixels/index.html      

## How to use
1. run the following command
```
bash
python tools.py --image test_image.jpg
```

   where test_image.jpg is the input image

2. it will output two files:

   the first is the ```test_image_superpixel.png``` which visualizes the mask

   the second is ```test_image.jpg.npy``` which is the narray of the mask
   (In each pixel, 
   it will contains a label which means the label of the superpixel it belongs to)

## Reference

Achanta R, Shaji A, Smith K, et al. SLIC superpixels compared to state-of-the-art superpixel methods[J]. IEEE transactions on pattern analysis and machine intelligence, 2012, 34(11): 2274-2282.
