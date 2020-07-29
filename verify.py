import os
import numpy as np

from solutions.problem_01 import (
        problem_01_method_01, problem_01_method_02
    )
from solutions.problem_02 import (
    problem_02_method_01, problem_02_method_02, problem_02_method_03
)
from utils.setup_utils import load_image, save_image, load_boxes

if __name__ == '__main__':

    problems = [1, 2]
    widths = [100, 250, 500, 1000, 2000]

    if not os.path.exists('output'):
        os.makedirs('output', exist_ok = True)

    print("Verifying solutions..")
    for problem_number in problems:
        for width in widths:

            img = load_image(width)
            
            if problem_number == 1:
                output_p01_m01 = problem_01_method_01(img)
                output_p01_m02 = problem_01_method_02(img)

                assert np.all(output_p01_m01 == output_p01_m02)

                save_image(output_p01_m01, 'problem_01_method_01', width)
                save_image(output_p01_m01, 'problem_01_method_02', width)

            if problem_number == 2:
                boxes = load_boxes(width)

                output_p02_m01 = problem_02_method_01(img, boxes)
                output_p02_m02 = problem_02_method_02(img, boxes)
                output_p02_m03 = problem_02_method_03(img, boxes)

                condition_1 =  np.all(output_p02_m01 == output_p02_m02)
                condition_2 =  np.all(output_p02_m03 == output_p02_m02)

                assert condition_1 and condition_2
                
                save_image(output_p02_m01, 'problem_02_method_01', width)
                save_image(output_p02_m02, 'problem_02_method_02', width)
                save_image(output_p02_m03, 'problem_02_method_03', width)

    print("All checks passed!")
