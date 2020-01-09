from poly import has_cuda

if has_cuda():
    try:
        from cuPy import *
    except ImportError:
        from numpy import *
else:
    from numpy import *
