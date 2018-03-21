"""
Tests for sparse.py

"""
import numpy as np
import scipy
from numpy.testing import assert_allclose
from nose.tools import raises

from mypackage import csr_matvec


class TestSparse:
    def setUp(self):
        self.m, self.n = 5, 6
        self.A = scipy.sparse.rand(self.m, self.n, density=0.4, format='csr')
        self.x = np.random.random_sample(self.n)

    def test_csr_matvec(self):
        matvec_computed = csr_matvec(self.A, self.x)
        matvec_scipy = self.A.dot(self.x)
        assert_allclose(matvec_computed, matvec_scipy)

    @raises(ValueError)
    def test_csr_matvec_value_error(self):
        x = np.random.random_sample(self.n+1)
        csr_matvec(self.A, x)


if __name__ == '__main__':
    import sys
    import nose

    argv = sys.argv[:]
    argv.append('--verbose')
    argv.append('--nocapture')
    nose.main(argv=argv, defaultTest=__file__)
