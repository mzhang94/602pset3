import sys
import numpy

class Viterbi():
    """
    decoder = Viterbi(W)
    u = decoder.decode(y)
    """
    def __init__(self,W):
        pass

    def back(self,x):
        """
        (x0,x1)=decoder.back(x) returns two possible previous states
        """
        pass
    
    def out(self,x):
        """
        (y0,y1)=decoder.out(x) returns two possible output sequences
        """
        pass
    
    def cost(self, bits, values):
        pass
    
    def decode(self,y):
        pass

    

if __name__ == "__main__":
    if len(sys.argv)==3:
        decoder = Viterbi(numpy.array(eval(sys.argv[1])))
        (u, Pmin, unique) = decoder.decode(numpy.array(eval(sys.argv[2])))
        print ''.join([str(x) for x in u]), \
        '   ( Pmin =',Pmin,', unique =',unique,')'
