# https://docs.python.org/3/library/decimal.html
from decimal import Decimal 
from decimal import getcontext

import numpy as np

b = 60

def minus_b():
    return -Decimal(b)

def square_root(): 
    return np.sqrt((Decimal(b)**2) - Decimal(2))

def x_plus(prec): 
    getcontext().prec = prec
    return minus_b() + square_root()

def x_minus(prec):
    getcontext().prec = prec
    return minus_b() - square_root()

def relative_error(function):
    return abs(function(5)-function(32))/abs(function(32))


def x_plus_better(prec): 
    getcontext().prec = prec
    return -Decimal(2)/(-minus_b() + square_root())

x = 4.16

def f(prec): 
    getcontext().prec = prec    
    return Decimal(x)**3 - Decimal(4)*Decimal(x)**2 + Decimal(.25)*Decimal(x) - Decimal(1)

def f_better(prec): 
    getcontext().prec = prec    
    y = Decimal(x) - Decimal(4)
    y = Decimal(x)*Decimal(y) + Decimal(.25)
    return Decimal(x)*Decimal(y) - Decimal(1)

