import numpy as np

def problem_02_method_01(img, boxes):
    """
    Solution for Method I of Problem #2 mentioned in 
    the blog.
    """
    output = img.copy()
    H, W = img.shape[:2]

    for box in boxes:
        top_h, top_w = box[0]
        bot_h, bot_w = box[1]
        for r in range(top_h, bot_h + 1):
            for c in range(top_w, bot_w + 1):
                if np.all(img[r, c, :] == [255, 0, 0]):
                    output[r, c, :] = [255, 255, 255]
                    
    return output

def problem_02_method_02(img, boxes):
    """
    Solution for Method II of Problem #2 mentioned in 
    the blog.
    """
    output = img.copy()

    for box in boxes:
        top_h, top_w = box[0]
        bot_h, bot_w = box[1]
        
        sub_img_inp = img[top_h: bot_h + 1, top_w: bot_w + 1] 
        sub_img_out = output[top_h: bot_h + 1, top_w: bot_w + 1]

        valid = np.all(sub_img_inp == [255, 0, 0], axis = -1)
        
        rs, cs = valid.nonzero()
        sub_img_out[rs, cs, :] = [255, 255, 255]

    return output

def problem_02_method_03(img, boxes):
    """
    Solution for Method III of Problem #2 mentioned in 
    the blog.
    """
    output = img.copy()

    valid = np.all(img == [255, 0, 0], axis = -1)
    rs, cs = valid.nonzero()

    all_valid_rcs = np.full(rs.shape, False)

    for box in boxes:
        top_h, top_w = box[0]
        bot_h, bot_w = box[1]
        
        cur_valid_rs = ((rs >= top_h) & (rs <= bot_h)) 
        cur_valid_cs = ((cs >= top_w) & (cs <= bot_w)) 
        cur_valid_rcs = cur_valid_rs & cur_valid_cs
        
        all_valid_rcs |= cur_valid_rcs

    rs = rs[all_valid_rcs]
    cs = cs[all_valid_rcs]

    output[rs, cs, :] = [255, 255, 255]

    return output
