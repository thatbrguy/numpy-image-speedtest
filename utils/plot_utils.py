import matplotlib.pyplot as plt
import numpy as np
import os

def create_plot(problem_number, zoom = False):

    text_color = 'black'
    widths = [100, 250, 500, 1000, 2000]

    filepath = os.path.join("plots", "problem_%02d_time.npy" % problem_number)
    method_times = np.load(filepath)

    plt.figure(figsize=(20, 10))
    
    if problem_number == 1:
        method_01_locs = [2.5 + 4*i for i in range(5)]
        method_02_locs = [3.5 + 4*i for i in range(5)]
        x_ticks_locs = [3 + 4*i for i in range(5)]

        m01_bars = plt.bar(method_01_locs, method_times[0], width = 1, color = '#C84C09')
        m02_bars = plt.bar(method_02_locs, method_times[1], width = 1, color = '#420217')
        
        plt.legend(['Method I', 'Method II'], fontsize = 22)

        if zoom:
            m02_speedups = method_times[0] / method_times[1]

            for idx, m02_bar in enumerate(m02_bars):
                
                plt.text(
                    m02_bar.get_x() + 0.13, 
                    m02_bar.get_height() + .005 / 4, 
                    "%dx" % m02_speedups[idx], fontsize = 18
                )

    elif problem_number == 2:
        method_01_locs = [2.5 + 4*i for i in range(5)]
        method_02_locs = [3.5 + 4*i for i in range(5)]
        method_03_locs = [4.5 + 4*i for i in range(5)]
        x_ticks_locs = [3.5 + 4*i for i in range(5)]
            
        m01_bars = plt.bar(method_01_locs, method_times[0], width = 1, color = '#436436')
        m02_bars = plt.bar(method_02_locs, method_times[1], width = 1, color = '#D2FF28')
        m03_bars = plt.bar(method_03_locs, method_times[2], width = 1, color = '#D6F599')
        
        plt.legend(['Method I', 'Method II', 'Method III'], fontsize = 22)

        if zoom:
            m02_speedups = method_times[0] / method_times[1]
            m03_speedups = method_times[0] / method_times[2]

            for idx, (m02_bar, m03_bar) in enumerate(zip(m02_bars, m03_bars)):
                
                plt.text(
                    m02_bar.get_x() + 0.13, 
                    m02_bar.get_height() + .005 / 4, 
                    "%dx" % m02_speedups[idx], fontsize = 18
                )

                plt.text(
                    m03_bar.get_x() + 0.13, 
                    m03_bar.get_height() + .005 / 4, 
                    "%dx" % m03_speedups[idx], fontsize = 18
                )

    plt.xticks(x_ticks_locs, widths, fontsize = 18, color = text_color)
    plt.yticks(fontsize = 18, color = text_color)
    
    plt.xlabel('Image Width (px)', fontsize = 25, color = text_color)
    plt.ylabel('Time Taken (s)', fontsize = 25, color = text_color)

    if zoom:
        plt.ylim(0, 0.1)

    filename = "problem_%02d" % problem_number
    if zoom:
        filename += "_zoomed"
    filename += ".png"

    plt.savefig(os.path.join("plots", filename))
