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

import numpy as np

def graph_function(f, precision=300, x1=-1, x2=1, y1=-1, y2=1):
    arx = np.fromfunction(lambda i: ((i-precision/2)/precision*2), (precision, ))
    ary = np.vectorize(f)(arx) 

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=16)

    plt.axis((x1,x2,y1,y2))
    plt.plot(arx, ary)
    plt.show()

def graph_two_functions(f1, f2, precision=300, x1=-1, x2=1, y1=-1, y2=1):
    arx = np.fromfunction(lambda i: ((i-precision/2)/precision*2), (precision, ))
    ary1 = np.vectorize(f1)(arx) 
    ary2 = np.vectorize(f2)(arx) 

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=16)

    plt.axis((x1,x2,y1,y2))
    plt.plot(arx, ary1)
    plt.plot(arx, ary2)
    plt.show()
