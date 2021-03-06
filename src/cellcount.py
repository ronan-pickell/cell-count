"""
This package takes a 2-dimensional binary array (0,1), and returns
the number of individually contiguous regions in that array which
contain the value of 1.

Usage:
    cellCount() accepts either a list or a numpy ndarray of 2 dimensions
    
    Example:
        import cellcount as cc

        number_of_cells = cc.countCells(img_array)

Author:
    Ronan Pickell - 10-29-2021

"""

import numpy as np

def fillCell(arr, start_point):
    '''Replaces a contiguous region of '1' values with '0' values
    
    Parameters:
        arr (list): 2D binary array
        start_point (tuple): row, column indices for starting fill point

    Returns:
        filled_arr (list): 2D binary array with filled in region
    
    '''
    x_start, y_start = start_point

    def fill_pixel(x,y):
        height, width = arr.shape

        if arr[x,y] == 0:
            return
        else:
            arr[x,y] = 0
            neighbor_coords = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
            for coords in neighbor_coords:
                if 0 <= coords[1] <= width-1 and 0 <= coords[0] <= height-1:
                    fill_pixel(coords[0],coords[1])

    fill_pixel(x_start, y_start)
    
    return arr


def countCells(arr):
    '''Returns the number of contiguous regions in an array that contain '1'
    
    Parameters:
        arr (list): 2D binary array

    Returns:
        cell_count (int): number of contiguous regions
    '''

    # Ensure array is a NumPy array
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)

    # Ensure array is 2 dimensional
    if arr.ndim != 2:
        raise Exception('Array must be 2-dimensional')
    
    # Ensure array is binary
    primary, secondary = np.array_equal(np.unique(arr),[0,1]), np.array_equal(np.unique(arr),[0,255])
    if not primary and not secondary:
        raise Exception('Array must be binary ([0,1] or [0,255])')
    elif secondary:
        arr = (arr==255).astype('int')

    cell_count = 0

    for r, row in enumerate(arr):
        for c, col in enumerate(row):
            if col == 1:
                arr = fillCell(arr, (r,c))
                cell_count += 1
    
    return cell_count
