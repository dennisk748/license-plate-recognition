# in segmentation we map out all the characters on the license plate and segemented into individual images.The concept of connected component analysis
# is also used here.

import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import cca


# invert the white pixels to black pixels and vice versa
license_plate = np.invert(cca.plate_like_objects[2])

labelled_plate = measure.label(license_plate)

fig, (ax1) = plt.subplots(1)
ax1.imshow(labelled_plate, cmap = "gray")

# the next lines are on the assuption that the width of a license plate should between 5% and 15% of the plate
# and height be between 35% and 60% this will eliminate some characters in the background
characterDimensions = (0.35*license_plate.shape[0],0.60*license_plate.shape[0],0.05*license_plate.shape[1],0.15*license_plate.shape[1])
minHeight, maxHeight, minWidth, maxWidth = characterDimensions

characters = []
counter = 0
column_list = []

for regions in regionprops(labelled_plate):
    y0, x0, y1, x1 = regions.bbox
    region_height = y1 - y0
    region_width = x1 - x0

    if region_height > minHeight and region_height < maxHeight and region_width > minWidth and region_width < maxWidth:
        roi = license_plate[y0:y1, x0:x1]

        #draw a red bordered triangle over the character
        rect_border = patches.Rectangle((x0,y0), region_width, region_height, edgecolor="red",linewidth=2,fill=False)

        ax1.add_patch(rect_border)

        #resize the character to be 20 by 20px
        resized_char = resize(roi, (20, 20))
        characters.append(resized_char)

        #to keep track of the arrangement of the characters
        column_list.append(x0)


plt.show()