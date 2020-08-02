import matplotlib.pyplot as plt
import numpy as np
import os

def create_plot(problem_number):
    """
    Function to that can be used to create plots after 
    the time measurements are completed.
    """
    fig, ax = plt.subplots(1, 2, figsize=(30, 7.5))

    create_subplot(problem_number, ax[0], zoom = False)
    create_subplot(problem_number, ax[1], zoom = True)

    plt.suptitle("Probelm %d Time Measurements" % problem_number, fontsize = 30)
    
    filename = "problem_%02d.png" % problem_number
    plt.savefig(os.path.join("plots", filename))

def create_subplot(problem_number, ax, zoom = False):
    """
    Function to that can be used to create subplots after 
    the time measurements are completed.
    """
    text_color = 'black'
    widths = [100, 250, 500, 1000, 2000]

    filepath = os.path.join("plots", "problem_%02d_time.npy" % problem_number)
    method_times = np.load(filepath)
    
    if problem_number == 1:
        method_01_locs = [2.5 + 4*i for i in range(5)]
        method_02_locs = [3.5 + 4*i for i in range(5)]
        x_ticks_locs = [3 + 4*i for i in range(5)]

        m01_bars = ax.bar(method_01_locs, method_times[0], width = 1, color = '#C84C09')
        m02_bars = ax.bar(method_02_locs, method_times[1], width = 1, color = '#420217')
        
        ax.legend(['Method I', 'Method II'], fontsize = 18)

        ## Plotting speedups if zoom is True.
        if zoom:
            m02_speedups = method_times[0] / method_times[1]

            for idx, m02_bar in enumerate(m02_bars):
                
                ax.text(
                    m02_bar.get_x() + 0.10, 
                    m02_bar.get_height() + .005 / 4, 
                    "%dx" % m02_speedups[idx], fontsize = 14
                )

    elif problem_number == 2:
        method_01_locs = [2.5 + 4*i for i in range(5)]
        method_02_locs = [3.5 + 4*i for i in range(5)]
        method_03_locs = [4.5 + 4*i for i in range(5)]
        x_ticks_locs = [3.5 + 4*i for i in range(5)]
            
        m01_bars = ax.bar(method_01_locs, method_times[0], width = 1, color = '#436436')
        m02_bars = ax.bar(method_02_locs, method_times[1], width = 1, color = '#D2FF28')
        m03_bars = ax.bar(method_03_locs, method_times[2], width = 1, color = '#D6F599')
        
        ax.legend(['Method I', 'Method II', 'Method III'], fontsize = 18)

        ## Plotting speedups if zoom is True.
        if zoom:
            m02_speedups = method_times[0] / method_times[1]
            m03_speedups = method_times[0] / method_times[2]

            for idx, (m02_bar, m03_bar) in enumerate(zip(m02_bars, m03_bars)):
                
                ax.text(
                    m02_bar.get_x() + 0.10, 
                    m02_bar.get_height() + .005 / 4, 
                    "%dx" % m02_speedups[idx], fontsize = 14
                )

                ax.text(
                    m03_bar.get_x() + 0.10, 
                    m03_bar.get_height() + .005 / 4, 
                    "%dx" % m03_speedups[idx], fontsize = 14
                )
    
    ax.set_xlabel('Image Width (px)', fontsize = 22, color = text_color)
    ax.set_ylabel('Time Taken (s)', fontsize = 22, color = text_color)

    ax.set_xticks(x_ticks_locs)
    ax.set_xticklabels(widths, fontsize = 18)

    ax.tick_params(axis = 'y', labelsize = 18)
    ax.tick_params(axis = 'x', labelsize = 18)

    if zoom:
        ax.set_ylim(0, 0.1)
