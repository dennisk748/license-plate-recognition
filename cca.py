# Connected component analysis/ blob extraction / region labeling / connected component labeling
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

# this gets all the connected regions and groups them together
label_image = measure.label(localization.binary_car_image)
#Here measure.label method was used to map all connected regions in the binary image file and label them.
plateDimensions = (0.08*label_image.shape[0], 0.2*label_image.shape[0],0.15*label_image.shape[1],0.4*label_image.shape[1])
minHeight, maxHeight, minWidth, maxWidth = plateDimensions
plate_objects_coordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.binary_car_image, cmap = "gray")

# here calling regionprops on the labelled image will return a list of all the regions as well as their properties
# like area, boundingbox, label, etc.
for region in regionprops(label_image):
    if region.area < 50:
        # then region is unlikely to be a license plate
        continue

    minRow, minCol, maxRow, maxCol = region.bbox
    region_height = maxRow - minRow
    region_width = maxCol - minCol
    # we use patches.Rectangle to draw a rectangle over all the mapped regions.
    if region_height >= minHeight and region_height <= maxHeight and region_width >= minWidth and region_width <= maxWidth and region_width > region_height:
        plate_like_objects.append(localization.binary_car_image[minRow:maxRow, minCol:maxCol])
        plate_objects_coordinates.append((minRow, minCol, maxRow, maxCol))
        rectBorder = patches.Rectangle((minCol, minRow), region_width, region_height, edgecolor = "red",linewidth=2,fill=False)
        ax1.add_patch(rectBorder)
    # lets draw a triangle over those regions
#although the headlamps are still showing so we need to do a vertical projection, since we know that the
#plates will have a much bigger number of pixels within them than the headlamps.
plt.show()