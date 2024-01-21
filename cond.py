import numpy as np
def get_color_grp_circle(circle_center, circle_radius, x,y):
    is_in_circle= ((x-circle_center[0])**2 + (y-circle_center[1])**2 )< circle_radius**2
    
    is_in_circle= (y > circle_center[1] )^ ( x > circle_center[0])

    color_grp_1= ['blue', 'cyan', 'white', 'steelblue', 'green', 'teal']
    color_grp_1=['blue']
    color_grp_2= ['red', 'orange', 'brown', 'yellow','black']
    # color_grp_2=['red']

    if is_in_circle:
        return color_grp_1
    else:
        return color_grp_2

def throw_some_sines(rows, cols,x,y):
    # sine_side=  abs(x-rows/2) + abs(y- cols/2) < rows//4 or abs(x) + abs(y) < cols//4 or abs(x-rows//3) + abs(y) < rows//4
    sine_side= abs(x -rows/2) + abs(y- cols) < rows//3 and abs(x -rows/2) + abs(y- cols) > rows//2 
    color_grp_1= ['blue', 'cyan', 'white', 'steelblue', 'green', 'teal']
    color_grp_2= ['red', 'orange', 'brown', 'yellow','black']
    if sine_side:
        return color_grp_1
    else:
        return color_grp_2

def sine_side(rows, cols, x, y):
    
    x= x- cols/2
    y= y- rows/2 

    amp = rows/2
    period = (2*np.pi)/cols
    decider=  y > amp*np.sin(period*x)
    color_grp_1= ['blue', 'cyan', 'white', 'steelblue', 'green', 'teal']
    color_grp_2= ['red', 'orange', 'brown', 'yellow','black']
    if sine_side:
        return color_grp_1
    else:
        return color_grp_2

def grids(rows,cols,x ,y ):
    pos_x= 0
    pos_y= y//100
    color_grp_1= ['cyan', 'white', 'green', 'teal']
    color_grp_2= ['red', 'orange', 'brown', 'yellow','black']
    color_grp_3= ['black', 'purple', 'indigo', 'deeppink']
    color_grp_4= ['black', 'red', 'maroon', 'orange']
    color_grp_5=['orange', 'white', 'green']
    color_grp_6= ['red','green', 'skyblue', 'cyan', 'yellow','orange', 'white', 'black','gray']
    return color_grp_6
    if (pos_x+ pos_y)%2:
        return color_grp_1
    else:
        return color_grp_2