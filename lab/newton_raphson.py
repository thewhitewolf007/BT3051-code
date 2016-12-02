def newton_raphson(f,x0,TOL=1e-5):
    """Computes the zero of a function using the newton raphson method
    >>> newton_raphson(lambda x: x*x*x-9,2)
    2.0800838230887337
    """
    x=x0
    def _derv(f,x,h=1e-5):
        return (f(x+h)-f(x))/h
    while (abs(f(x))>TOL):
        x=x-(f(x)/_derv(f,x,TOL))
    return(x)

import doctest

if __name__=='__main__':
	doctest.testmod(verbose=True)
