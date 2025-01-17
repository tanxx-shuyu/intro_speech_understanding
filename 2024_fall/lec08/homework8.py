import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    # Create a grid of indices k and n
    k = np.arange(N).reshape((N, 1))  # Column vector of indices
    n = np.arange(N)                  # Row vector of indices

    # Compute the exponent for each element
    exponent = -2j * np.pi * k * n / N

    # Compute the DFT matrix using the exponential function
    W = np.exp(exponent)

    return W