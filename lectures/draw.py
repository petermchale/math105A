from matplotlib import pyplot as plt


def create_figure(width=10, height=8, fontsize=20, fontsize_tick=15):
    fig = plt.figure(figsize=(width, height), facecolor='w')
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=fontsize_tick)
    return fig, ax, fontsize, fontsize_tick


def create_two_figures(width=20, height=8, fontsize=20, fontsize_tick=15):
    fig = plt.figure(figsize=(width, height), facecolor='w')
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.tick_params(labelsize=fontsize_tick)
    ax2.tick_params(labelsize=fontsize_tick)
    return fig, ax1, ax2, fontsize, fontsize_tick
