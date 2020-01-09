from poly import has_cuda

if has_cuda():
    try:
        from cuML import *
    except ImportError:
        from sklearn import *
else:
    from sklearn import *
