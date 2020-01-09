from poly import has_cuda

if has_cuda():
    try:
        from cuDF import *
    except ImportError:
        from pandas import *
else:
    from pandas import *
