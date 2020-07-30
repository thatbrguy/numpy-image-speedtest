import os
import cv2
import numpy as np

def load_image(width):
    """
    Loads the image from the data folder given the width value.
    """
    assert width in {2000, 1000, 500, 250, 100}, \
        "Please select a valid width! [Choices: 2000, 1000, 500, 250 or 100]"

    path = os.path.join(os.getcwd(), "data", "img_%s.png" % width)
    img = cv2.cvtColor(cv2.imread(path, 1), cv2.COLOR_BGR2RGB)

    return img

def save_image(img, problem_method, width):
    """
    Saves the image to the output folder given the problem_method 
    string and the width value.
    """
    path = os.path.join(os.getcwd(), "output", "%s_%s.png" % (problem_method, width))
    cv2.imwrite(path, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def load_boxes(width):
    """
    Returns a NumPy array with the top-left and bottom-right coordinates
    of the five boxes defined in Problem #2.
    """
    assert width in {2000, 1000, 500, 250, 100}, \
        "Please select a valid width! [Choices: 2000, 1000, 500, 250 or 100]"

    ## For all our images, height is half the width value.
    height = width // 2

    ## Creating convenient variables to define box coordinates.
    h, w = height / 10, width / 10

    ## List of 5 elements each defining one box. Each element of the list
    ## has two lists representing two coordinates. The first coordinate 
    ## represents the top-left corner of the box. The second coordinate 
    ## represents the bottom-right corner of the box.
    boxes = np.array([
        [[h, w], [9*h, 2*w]],
        [[6.5*h, 2.5*w], [9*h, 8*w]],
        [[h, 2.5*w], [5.5*h, 6*w]],
        [[h, 6.5*w], [5.5*h, 9*w]],
        [[6.5*h, 8.5*w], [9*h, 9*w]]
    ]).astype(np.int32)

    return boxes
