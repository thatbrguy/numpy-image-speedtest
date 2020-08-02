import os
import timeit
import numpy as np
from tqdm import tqdm
from textwrap import dedent

from utils.plot_utils import create_plot

def get_setup_string(width):
    """
    Returns the setup string for the given width.
    """
    setup = \
    """
    from solutions.problem_01 import (
        problem_01_method_01, problem_01_method_02
    )
    from solutions.problem_02 import (
        problem_02_method_01, problem_02_method_02, problem_02_method_03
    )
    from utils.setup_utils import load_image, load_boxes
    width = %s
    img = load_image(width)
    boxes = load_boxes(width)
    """ % width

    setup = dedent(setup)

    return setup

if __name__ == "__main__":

    problems = [1, 2]
    widths = [100, 250, 500, 1000, 2000]

    if not os.path.exists('plots'):
        os.makedirs('plots', exist_ok = True)

    for problem_number in problems:

        if problem_number == 1:
            methods = [[], []]
        elif problem_number == 2:
            methods = [[], [], []]
        
        for width in tqdm(widths, desc = "[Problem %02d]: Calculating Time Taken" % problem_number):
        
            setup = get_setup_string(width)

            if problem_number == 1:
                p01_m01 = timeit.repeat("problem_01_method_01(img)", setup = setup, number = 1, repeat = 3)
                p01_m02 = timeit.repeat("problem_01_method_02(img)", setup = setup, number = 1, repeat = 3)

                methods[0].append(min(p01_m01))
                methods[1].append(min(p01_m02))
            
            elif problem_number == 2:
                p02_m01 = timeit.repeat("problem_02_method_01(img, boxes)", setup = setup, number = 1, repeat = 3)
                p02_m02 = timeit.repeat("problem_02_method_02(img, boxes)", setup = setup, number = 1, repeat = 3)
                p02_m03 = timeit.repeat("problem_02_method_03(img, boxes)", setup = setup, number = 1, repeat = 3)

                methods[0].append(min(p02_m01))
                methods[1].append(min(p02_m02))
                methods[2].append(min(p02_m03))

        ## Printing stats only for width = 2000. You may edit this part to 
        ## print stats for other width sizes as well. The plots display
        ## stats for all width sizes.
        print("==============================")
        print("[Problem %02d]: For width = 2000, calculated times are:" % problem_number)
        for i, method in enumerate(methods, 1):
            print("[Problem %02d]: Method %d: %.3fs"% (problem_number, i, method[-1]))
        print("==============================")

        methods = np.array(methods)
        
        filename = "problem_%02d_time.npy" % problem_number
        output_path = os.path.join(os.getcwd(), 'plots', filename)
        np.save(output_path, methods)

        create_plot(problem_number)
