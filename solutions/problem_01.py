import numpy as np

def problem_01_method_01(img):
    """
    Solution for Method I of Problem #1 mentioned in 
    the blog.
    """
    output = img.copy()
    
    H, W = img.shape[:2]
    for r in range(H):
        for c in range(W):
            if np.all(img[r, c, :] == [255, 0, 0]):
                output[r, c, :] = [255, 255, 255]

    return output

def problem_01_method_02(img):
    """
    Solution for Method II of Problem #1 mentioned in 
    the blog.
    """
    output = img.copy()

    valid = np.all(img == [255, 0, 0], axis = -1)
    rs, cs = valid.nonzero()
    output[rs, cs, :] = [255, 255, 255]

    return output
