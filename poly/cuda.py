from poly import has_cuda

if has_cuda():
    from numba.cuda import *
