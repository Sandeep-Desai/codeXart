import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
from tqdm import trange

from art import find_closest, filter_image, create_gif
from cond import throw_some_sines, get_color_grp_circle, sine_side, grids, mask_to_arr, mask


image_path= './assets/lal_minar.jpg'

image=Image.open(image_path)

image_arr= np.array(image)
image_arr= image_arr/ 255
# # print(image_arr[0][0])

# # print(find_closest(image_arr[0][0]))

approx_arr= np.zeros(shape=image_arr.shape)

rows, cols= image_arr.shape[:2]

mask_arr= mask_to_arr('assets/mask-7.png', rows,cols)

print(mask_arr.shape)
print(image_arr.shape)
for i in trange(rows):
    for j in range(cols):
        # color_grp= get_color_grp_circle((rows//2,cols//2),rows//4,i,j)
        # color_grp= grids(rows,cols,i,j)
        color_grp= mask(mask_arr[i][j])
        approx_arr[i][j]= find_closest(image_arr[i][j], color_grp)

# # approx_arr= find_closest(image_arr)



plt.imshow(approx_arr)
plt.show()
plt.imsave(fname=f'results/lal_minar-mask-2.png',arr=approx_arr)