from poly import has_cuda

if has_cuda():
    try:
        from cuGraph import *
    except ImportError:
        from networkx import *
else:
    from networkx import *
