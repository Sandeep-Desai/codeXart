from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import colors as mcolors
from tqdm import trange
import os
from cond import mask, mask_to_arr

def find_closest(pixel, color_grp:list):
    '''
    function to find the closest color to the pixel from the provided list of colors
    '''
    # https://matplotlib.org/stable/gallery/color/named_colors.html
    # common_colors = ['yellow', 'orange','red','brown' ,'black','purple']
    common_colors = color_grp

    # common_colors=common_colors[:5]
    cost = 1000000000000
    closest_value= (255,255,255)
    color=''
    for color_name in common_colors:
        rgb_values = mcolors.to_rgb(color_name)
        cur_cost = np.sqrt((rgb_values[:3]- pixel)**2).sum()
        if cur_cost< cost:
            color=color_name
            cost= cur_cost
            closest_value= rgb_values
    return closest_value

def filter_image(image_arr, mask_arr):
    image_arr= image_arr/ 255
    approx_arr= np.zeros(shape=image_arr.shape)

    rows, cols= image_arr.shape[:2]

    for i in trange(rows):
        for j in range(cols):
            color_grp= mask(mask_arr[i][j])
            approx_arr[i][j]= find_closest(image_arr[i][j], color_grp)
    return approx_arr

def decode_gif_file(filename,frame):
        img = Image.open(filename)
        print(img)
        img.seek(frame)
        return img, 2

def create_gif(input_file_path, output_file_path):
    
    img,frame= decode_gif_file(input_file_path,1)
    while(True):
        try:
            img,f= decode_gif_file('matt.gif',frame)

            filtered_img=filter_image(np.array(img))

            plt.imsave(f'output_file_path/{frame}.png', filtered_img)
            # plt.show()
            frame+=1
        except Exception as e:
            print(e.with_traceback())
            break

def gif_static(main_image_file, mask_file):
    img,frame= decode_gif_file(mask_file,1)
    
    main_image= Image.open(main_image_file)

    main_image_arr= np.array(main_image)

    print(main_image_arr.shape)

    img,frame= decode_gif_file(mask_file,1)

    while(True):
        try:
            print(frame)
            img,f= decode_gif_file(mask_file,frame)

            img_res= img.resize(reversed(main_image_arr.shape[:2]))

            # mask_img=filter_image(np.array(img))
            
            mask_arr= np.array(img_res)
            mask_arr= mask_arr/255
            print(mask_arr.shape, main_image_arr.shape)

            result_img= filter_image(main_image_arr, mask_arr)

            plt.imsave(f'results/lal_minar_gif_2/{frame}.png', result_img)
            # plt.show()
            frame+=1
        except Exception as e:
            print(e.with_traceback())
            break