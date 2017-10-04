def different_sign(a, b):
        return a * b < 0

def print_heading(): 
    print('a_n\t\t', \
          'b_n\t\t', \
          'p_n\t\t', 
          'f(p_n)')
    
def print_row(func, low, high, midpoint): 
    print('%6f\t' % low, \
          '%6f\t' % high, \
          '%6f\t' % midpoint, \
          '%6f\t' % func(midpoint))

