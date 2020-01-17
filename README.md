# poly
Automatic GPU Acceleration for Python (if supported)


## Usage
Poly tries to wrap libraries that are compatible with popular Python packages, but offer GPU support.  The API should be the same.  Which library is imported is determined by if the host has GPU support or not.

Below are some of the libraries imported
```
from poly import has_cuda
has_cuda()

from poly import numpy
from poly import tf
from poly import networkx
from poly import sklearn
from poly import spacy
from poly import keras
from poly import pandas
```
