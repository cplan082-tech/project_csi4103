from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

from PIL import Image
import cv2

image1 = cv2.imread('Test_image.jpg')

# Modify Picture 2 to match dimensions Picture 1 so MSE can be calculated
image2 = Image.open('pot_2_drawn.png')

img_resize = image2.resize((image1.shape[1], image1.shape[0]))
rgb_im = img_resize.convert('RGB')
rgb_im.save('drawn_pot_cropped.jpg')

