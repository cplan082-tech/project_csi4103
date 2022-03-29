import skimage
from skimage import metrics
from PIL import Image
from skimage import io

img1 = io.imread('image_1.png')
img2 = io.imread('image_2.png')

print(skimage.metrics.mean_squared_error(img1, img2))
