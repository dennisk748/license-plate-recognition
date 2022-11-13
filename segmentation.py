# in segmentation we map out all the characters on the license plate and segemented into individual images.The concept of connected component analysis
# is also used here.

import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import cca