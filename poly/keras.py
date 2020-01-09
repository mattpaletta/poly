from poly import has_cuda

# If we have cuda, use the tensorflow backend
if has_cuda():
    import os
    try: 
        import plaidml.keras
        plaidml.keras.install_backend()
    except ImportError:
        pass
from keras import *
