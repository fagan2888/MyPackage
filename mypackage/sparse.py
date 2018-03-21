"""
Routines for sparse matrices

"""
import numpy as np
import scipy.sparse
from numba import jit, prange


def csr_matvec(A, x):
    A = scipy.sparse.csr_matrix(A)
    m, n = A.shape
    if len(x) != n:
        raise ValueError('dimensions do not match')
    out = np.empty(m)
    _csr_matvec(m, A.data, A.indices, A.indptr, x, out)
    return out


@jit(nopython=True, parallel=True)
def _csr_matvec(num_rows, data, indices, indptr, x, out):
    for i in prange(num_rows):
        dot_prod = 0
        for k in range(indptr[i], indptr[i+1]):
            dot_prod += data[k] * x[indices[k]]
        out[i] = dot_prod
    return out
