import numpy as np
import imageio
from skimage.filters import sobel
from skimage import morphology
import os

#this code was modified from https://scikit-image.org/docs/0.12.x/auto_examples/xx_applications/plot_coins_segmentation.html

def inverted_color(img): #The edge segmentation algorithm treats white as the important regions, so invert image to get empahsis on dark regions (cracks)
    img = img.astype('float32')
    return 255 - img

file_array = []

import os
# return all files as a list
for file in os.listdir("/Users/nicolasouellet/Documents/capstone/edge_detection/method_2_scikit/"):
     # check the files which are end with specific extension
    if file.endswith(".png"):
        #append path name of selected files
        file_array.append(file)

#SORTING FILE LIST
# extract the number and create a tuple
file_tuple = [(int(s[12:15]), s) for s in file_array]
# sort the tuple and create a new list with only the filename
sorted_file_array = [x[1] for x in sorted(file_tuple)]

for i,png in enumerate(sorted_file_array):
    print("Getting edge map of", png)
    
    coins = inverted_color(imageio.imread(png))
    elevation_map = sobel(coins) #get edge map

    markers = np.zeros_like(coins) #filter out dark colors
    markers[coins < 180] = 1
    markers[coins >= 180] = 2

    segmentation = morphology.watershed(elevation_map, markers) #group lighter colors together to get a mask of the cracks

    name_of_file = "edge_map_%d.png" % (540001 + i)
    path = "/Users/nicolasouellet/documents/capstone/edge_detection/method_2_scikit/edge"
    imageio.imwrite(os.path.join(path,name_of_file),segmentation, format="png")
