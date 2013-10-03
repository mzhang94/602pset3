import sys
import numpy

def conv(W,u):
    """
    y = conv(W,u)
    W: r-by-K 0/1 numpy array 0/1 (for convolution code )
    u: 0/1 numpy vector of length T (binary input to be encoded)
    y: 0/1 numpy vector of length T*r (convolutional encoding of u)
    """
    return numpy.array([numpy.convolve(row, u)[0:len(u)] % 2 for row in W]).flatten('F')
	

    

if __name__ == "__main__":
    if len(sys.argv)>2:
        W = numpy.array(eval(sys.argv[1]))
        u = numpy.array([int(x) for x in sys.argv[2]])
        print ''.join([str(int(x)) for x in conv(W,u)])

    
    
